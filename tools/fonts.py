#!/usr/bin/env python3
"""디스플레이 서체를 이 사이트가 실제로 쓰는 글자만큼으로 줄인다.

한글 웹폰트는 통째로 받으면 2MB 급이다. 그래서 두 가지를 한다.

1. **라틴과 한글을 따로 낸다.** `unicode-range` 가 붙어 있으면 브라우저는 그
   페이지에 실제로 있는 문자에 해당하는 파일만 받는다. 영문 페이지는 한글
   파일을 아예 받지 않는다.
2. **한글은 쓰는 글자만 남긴다.** 상용 2350자를 다 넣으면 1MB 인데, 이 사이트가
   쓰는 것은 그 4분의 1도 안 된다.

2 번의 대가는 명확하다 — **콘텐츠에 새 글자가 들어오면 폰트를 다시 만들어야
한다.** 잊으면 그 글자만 시스템 폰트로 떨어져 조용히 어긋난다. 그래서
`--check` 가 있고, CI 가 빌드 전에 그걸 돌린다. 빠진 글자는 경고가 아니라
에러다.

    python3 tools/fonts.py            # 내려받고 서브셋을 다시 만든다
    python3 tools/fonts.py --check    # 커버리지만 확인한다 (네트워크 불필요)
"""

import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "fonts"
CACHE = Path("/tmp/sqzer-fonts")

# Noto Sans KR Variable. wght 100~900 이 한 파일에 있어서, 초경량 제목부터
# 굵은 라벨까지 파일 하나로 낸다.
SRC_URL = "https://github.com/google/fonts/raw/main/ofl/notosanskr/NotoSansKR%5Bwght%5D.ttf"
SRC = CACHE / "NotoSansKR.ttf"

# 라틴·구두점·기호. 한글이 한 글자도 없는 페이지가 받는 전부.
LATIN = (
    "U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+2000-206F,"
    "U+20A0-20BF,U+2122,U+2190-21BB,U+2212,U+2500-257F,U+25A0-25FF,U+2605-2606"
)
# 한글 음절·자모·전각. 실제 쓰는 글자만 남기므로 범위가 아니라 --text 로 준다.
JAMO = "U+3130-318F,U+FF01-FF60"


def used_hangul() -> str:
    """content/ · templates/ · i18n/ 에 실제로 등장하는 한글 음절."""
    chars = set()
    for sub in ("content", "templates", "i18n"):
        for path in (ROOT / sub).rglob("*"):
            if path.suffix not in (".md", ".html", ".toml"):
                continue
            for ch in path.read_text(encoding="utf-8"):
                if "가" <= ch <= "힣":
                    chars.add(ch)
    return "".join(sorted(chars))


def subset(args: list[str], out: Path) -> None:
    subprocess.run(
        [sys.executable, "-m", "fontTools.subset", str(SRC),
         "--flavor=woff2", "--layout-features=*", f"--output-file={out}", *args],
        check=True,
    )
    print(f"  {out.name:24} {out.stat().st_size // 1024:>4} KB")


def check() -> int:
    """폰트가 콘텐츠의 모든 한글을 담고 있는지. 하나라도 없으면 에러."""
    from fontTools.ttLib import TTFont

    target = OUT / "display-kr.woff2"
    if not target.exists():
        print(f"{target} 가 없습니다 — python3 tools/fonts.py 를 먼저 돌리세요", file=sys.stderr)
        return 1

    covered = set()
    for table in TTFont(target)["cmap"].tables:
        covered |= set(table.cmap)

    missing = sorted(ch for ch in used_hangul() if ord(ch) not in covered)
    if missing:
        print(
            f"폰트에 없는 글자 {len(missing)}자: {''.join(missing[:40])}"
            f"{'…' if len(missing) > 40 else ''}\n"
            "python3 tools/fonts.py 로 서브셋을 다시 만드세요.",
            file=sys.stderr,
        )
        return 1
    print(f"ok — 한글 {len(used_hangul())}자 전부 포함")
    return 0


def build() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    if not SRC.exists():
        print(f"내려받는 중: {SRC_URL}")
        urllib.request.urlretrieve(SRC_URL, SRC)

    hangul = used_hangul()
    print(f"쓰는 한글 {len(hangul)}자")
    subset([f"--unicodes={LATIN}"], OUT / "display-latin.woff2")
    subset([f"--unicodes={JAMO}", f"--text={hangul}"], OUT / "display-kr.woff2")
    return 0


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv else build())
