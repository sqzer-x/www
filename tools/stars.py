#!/usr/bin/env python3
"""프로젝트의 GitHub 별 개수를 front matter 에 적어 넣는다.

**왜 빌드 시점인가.** 브라우저에서 부르면 익명 GitHub API 는 IP 당 시간당
60회다. 한국은 CGNAT 이 흔해서 한 사람이 아니라 한 회선이 그 한도를 나눠 쓰고,
걸리면 별이 전부 빈칸으로 남는다. 그리고 sqzass 는 같은 입력이면 같은 바이트를
내야 하는데, 렌더 중에 네트워크를 부르면 그 보장이 깨진다.

그래서 숫자를 레포에 커밋해 둔다. 빌드는 파일만 읽으므로 재현되고, 값은
`.github/workflows/stars.yml` 이 하루 한 번 갱신한다.

0 이어도 적는다. 그게 사실이고, 없는 항목만 숫자가 빠지면 줄이 어긋난다.

    python3 tools/stars.py            # 갱신
    python3 tools/stars.py --check    # 모든 repo 항목에 숫자가 있는지 확인
"""

import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# content/ 전체를 훑는다. 별 개수는 프로젝트 상세 페이지에도 있고 홈의 모자이크
# 카탈로그에도 있는데, 후자를 빼 두면 홈의 숫자만 조용히 낡는다.
CONTENT = ROOT / "content"

# `repo<공백>= "https://github.com/owner/name"` — 뒤따르는 stars 줄까지 함께 잡아
# 갈아 끼운다. 없으면 새로 붙인다.
LINE = re.compile(
    r'^(?P<indent>[ \t]*)repo(?P<pad>\s*)= "https://github\.com/(?P<slug>[^/"]+/[^/"]+)"'
    r'(?P<old>\n[ \t]*stars\s*=\s*\d+)?',
    re.M,
)


def fetch(slug: str) -> int | None:
    """gh 가 있으면 그걸 쓴다 — 인증 요청은 5000/시간이라 CI 에서 안 걸린다."""
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{slug}", "--jq", ".stargazers_count"],
            capture_output=True, text=True, timeout=20,
        )
        if out.returncode == 0 and out.stdout.strip().isdigit():
            return int(out.stdout.strip())
    except (OSError, subprocess.SubprocessError):
        pass
    try:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{slug}",
            headers={"Accept": "application/vnd.github+json", "User-Agent": "sqzer.com"},
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            return int(json.load(r)["stargazers_count"])
    except Exception as e:
        print(f"  {slug}: {e}", file=sys.stderr)
        return None


def check() -> int:
    bad = [
        f"{p.relative_to(ROOT)} ({m.group('slug')})"
        for p in sorted(CONTENT.rglob("*.md"))
        for m in LINE.finditer(p.read_text(encoding="utf-8"))
        if not m.group("old")
    ]
    if bad:
        print("별 개수가 없는 항목:\n  " + "\n  ".join(bad) +
              "\npython3 tools/stars.py 를 돌리세요.", file=sys.stderr)
        return 1
    print("ok — 모든 프로젝트에 별 개수가 있습니다")
    return 0


def main() -> int:
    cache: dict[str, int | None] = {}
    changed = 0

    for path in sorted(CONTENT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")

        def swap(m: re.Match) -> str:
            slug = m.group("slug")
            if slug not in cache:
                cache[slug] = fetch(slug)
            n = cache[slug]
            if n is None:
                return m.group(0)  # 못 가져오면 있던 값을 지우지 않는다
            keep = m.group(0)[: m.start("old") - m.start()] if m.group("old") else m.group(0)
            # `stars` 가 `repo` 보다 한 글자 길다. 여백을 그대로 베끼면 = 열이
            # 한 칸 밀린다 — 이 카탈로그들은 = 를 맞춰 적는 손글씨 TOML 이다.
            pad = m.group("pad")
            return f'{keep}\n{m.group("indent")}stars{pad[1:] or " "}= {n}'

        new = LINE.sub(swap, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1

    for slug, n in sorted(cache.items()):
        print(f"  {slug:28} {n if n is not None else '실패'}")
    print(f"{changed}개 파일 갱신")
    return 0


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv else main())
