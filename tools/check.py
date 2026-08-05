#!/usr/bin/env python3
"""빌드가 잡아 주지 않는 세 가지를 검사한다.

sqzass 는 마크다운의 `@/` 링크와 템플릿 변수와 에셋 이름을 전부 확인하고 틀리면
빌드를 세운다. 확인하지 않는 것은 `[extra]` 안이다 — 거기는 생성기가 읽지 않는
자유 테이블이라, 프로젝트 카탈로그의 url 오타는 조용히 배포된다.

i18n 도 마찬가지로 반쪽이다. 템플릿이 실제로 부르는 키가 없으면 빌드가 서지만,
어느 템플릿도 아직 안 부르는 키가 한쪽 언어에만 있는 것은 그냥 지나간다. 그
상태는 그 키를 처음 쓰는 날 빌드를 세운다.

세 번째는 템플릿이 손으로 쓴 링크다. sqzass 는 마크다운의 `@/` 는 확인해 주지만
`href="{{ home }}"` 처럼 템플릿이 조립한 주소는 확인하지 않는다. 한국어 홈을
없앤 날 로고 링크가 열한 장에서 `/ko/` 를 가리킨 채로 남았고, 빌드도 CI 도
아무 말을 하지 않았다. public/ 이 있을 때만 돈다 — 없으면 조용히 건너뛴다.

    python3 tools/check.py
"""

import re
import sys
import tomllib
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = {"en": "", "ko": "/ko"}  # 코드 → URL 접두사
fails = []


def front_matter(path: Path) -> dict:
    """`+++` 로 감싼 TOML 머리말만 떼어 읽는다."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++"):
        return {}
    end = text.find("+++", 3)
    if end == -1:
        fails.append(f"{path.relative_to(ROOT)}: 닫히지 않은 +++ 머리말")
        return {}
    return tomllib.loads(text[3:end])


def catalog_urls(fm: dict) -> set:
    """카탈로그가 주장하는 프로젝트 URL 전부."""
    extra = fm.get("extra", {})
    urls = {item["url"] for item in extra.get("featured", [])}
    for group in extra.get("group", []):
        urls |= {item["url"] for item in group.get("item", [])}
    return urls


def check_projects():
    """카탈로그와 실제 페이지가 양방향으로 일치하는지."""
    projects = ROOT / "content" / "projects"
    for lang, prefix in LANGS.items():
        suffix = ".ko.md" if lang == "ko" else ".md"
        index = projects / ("_index.ko.md" if lang == "ko" else "_index.md")
        if not index.exists():
            fails.append(f"{index.relative_to(ROOT)} 가 없습니다")
            continue

        claimed = catalog_urls(front_matter(index))
        actual = {
            f"{prefix}/projects/{p.name[: -len(suffix)]}/"
            for p in projects.glob(f"*{suffix}")
            if not p.name.startswith("_index")
            # en 패스에서 `foo.ko.md` 가 `foo.ko` 로 잡히지 않게 거른다.
            and (lang == "ko" or not p.name.endswith(".ko.md"))
        }

        for url in sorted(claimed - actual):
            fails.append(f"[{lang}] 카탈로그가 가리키는 페이지가 없습니다: {url}")
        for url in sorted(actual - claimed):
            fails.append(f"[{lang}] 페이지가 카탈로그에 없습니다: {url}")


def check_preview():
    """홈의 미리보기·모자이크 카탈로그가 실제 페이지와 파일을 가리키는지.

    이것도 [extra] 라 생성기가 안 읽는다. url 이 어긋나면 에러가 아니라 그냥
    미리보기가 안 나오고, 그건 배포된 뒤에야 눈으로만 보인다.
    """
    for lang, prefix in LANGS.items():
        index = ROOT / "content" / ("_index.ko.md" if lang == "ko" else "_index.md")
        if not index.exists():
            continue  # 그 언어에 첫 화면이 없을 수 있다. 한국어가 그렇다.
        extra = front_matter(index).get("extra", {})
        for item in extra.get("mosaic", []):
            slug = item["url"].rstrip("/").rsplit("/", 1)[-1]
            suffix = ".ko.md" if lang == "ko" else ".md"
            if not (ROOT / "content" / "projects" / f"{slug}{suffix}").exists():
                fails.append(f"[{lang}] 모자이크가 가리키는 프로젝트가 없습니다: {item['url']}")
            for key in ("cover", "mark"):
                if item[key] and not (ROOT / "static" / item[key]).exists():
                    fails.append(f"[{lang}] 모자이크 {key} 파일이 없습니다: {item[key]}")

        for item in extra.get("preview", []):
            url = item["url"]
            slug = url.rstrip("/").rsplit("/", 1)[-1]
            suffix = ".ko.md" if lang == "ko" else ".md"
            if not (ROOT / "content" / "posts" / f"{slug}{suffix}").exists():
                fails.append(f"[{lang}] 미리보기가 가리키는 글이 없습니다: {url}")
            for key in ("poster", "video"):
                if not (ROOT / "static" / item[key]).exists():
                    fails.append(f"[{lang}] 미리보기 {key} 파일이 없습니다: {item[key]}")


def check_i18n():
    """두 언어의 키 집합이 같은지. 다르면 그 키를 처음 쓰는 날 빌드가 선다."""
    keys = {}
    for lang in LANGS:
        path = ROOT / "i18n" / f"{lang}.toml"
        if not path.exists():
            fails.append(f"{path.relative_to(ROOT)} 가 없습니다")
            return
        keys[lang] = set(tomllib.loads(path.read_text(encoding="utf-8")))

    a, b = LANGS
    for key in sorted(keys[a] - keys[b]):
        fails.append(f"i18n: '{key}' 가 {a} 에만 있습니다")
    for key in sorted(keys[b] - keys[a]):
        fails.append(f"i18n: '{key}' 가 {b} 에만 있습니다")


def check_links():
    """빌드된 HTML 의 내부 링크가 전부 실제 파일에 닿는지.

    디렉터리가 있는 것과 페이지가 있는 것은 다르다 — public/ko/ 는 하위 갈래
    때문에 존재하지만 그 안에 index.html 이 없으면 그 주소는 404 다. 처음 짠
    검사는 exists() 를 써서 이걸 통과시켰고, 그래서 죽은 링크가 하나 배포됐다.
    is_file() 로 묻는다.
    """
    pub = ROOT / "public"
    if not pub.is_dir():
        return

    dead = {}
    for f in pub.rglob("*.html"):
        for href in re.findall(r'href="([^"#?]+)', f.read_text(encoding="utf-8")):
            if href.startswith(("http", "mailto:", "#", "//")):
                continue
            t = pub / urllib.parse.unquote(href).lstrip("/")
            if not (t.is_file() or (t / "index.html").is_file()):
                dead.setdefault(href, set()).add(str(f.relative_to(pub)))

    for href, pages in sorted(dead.items()):
        where = ", ".join(sorted(pages)[:3]) + ("…" if len(pages) > 3 else "")
        fails.append(f"죽은 내부 링크: {href}  ({len(pages)}장: {where})")


check_projects()
check_preview()
check_i18n()
check_links()

if fails:
    print("\n".join(fails), file=sys.stderr)
    sys.exit(1)
print("ok")
