#!/usr/bin/env python3
"""빌드가 잡아 주지 않는 두 가지를 검사한다.

sqzass 는 마크다운의 `@/` 링크와 템플릿 변수와 에셋 이름을 전부 확인하고 틀리면
빌드를 세운다. 확인하지 않는 것은 `[extra]` 안이다 — 거기는 생성기가 읽지 않는
자유 테이블이라, 프로젝트 카탈로그의 url 오타는 조용히 배포된다.

i18n 도 마찬가지로 반쪽이다. 템플릿이 실제로 부르는 키가 없으면 빌드가 서지만,
어느 템플릿도 아직 안 부르는 키가 한쪽 언어에만 있는 것은 그냥 지나간다. 그
상태는 그 키를 처음 쓰는 날 빌드를 세운다.

    python3 tools/check.py
"""

import sys
import tomllib
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


check_projects()
check_i18n()

if fails:
    print("\n".join(fails), file=sys.stderr)
    sys.exit(1)
print("ok")
