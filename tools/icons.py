#!/usr/bin/env python3
"""로고 원본에서 마스크 자산과 파비콘을 만든다.

원본은 **흰 배경에 검은 선화**다. 알파 채널이 있지만 전부 불투명이라, 알파를
형태로 읽으면 마크가 단색 사각형으로 나오고 여백 트림도 안 먹는다. 형태는
명도에 있으므로 명도를 뒤집어 알파로 쓴다. (이걸 세 번 틀려서 스크립트가 됐다.)

마크는 마스크로만 나간다. 선 색은 CSS 가 정하고, 규칙은 하나다 — **다크면 흰
선, 라이트면 검은 선. 중간 회색은 없다.** 회색 선화는 비활성 상태로 읽힌다.

파비콘에는 CSS 가 닿지 않고 투명 배경은 브라우저 탭 색에 따라 사라진다. 그래서
불투명 판을 깔고 두 벌을 낸다 — 밝은 탭에는 검은 판에 흰 선, 어두운 탭에는 흰
판에 검은 선.

    python3 tools/icons.py [원본디렉터리]      # 기본 ~/Downloads
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "static" / "images"
SRC_DIR = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/himesama/Downloads")

INK = (16, 20, 26)
PAPER = (232, 236, 241)


def shape(path: Path) -> Image.Image:
    """선화를 알파 마스크로. 흰 배경 위에 합성한 뒤 명도를 뒤집는다."""
    im = Image.open(path).convert("RGBA")
    flat = Image.alpha_composite(Image.new("RGBA", im.size, (255,) * 4), im).convert("L")
    a = ImageOps.invert(flat).point(lambda v: 0 if v < 24 else min(255, int(v * 1.35)))
    return a.crop(a.getbbox())


def write_mask(alpha: Image.Image, dst: Path, width: int) -> None:
    h = max(1, round(alpha.height * width / alpha.width))
    a = alpha.resize((width, h), Image.LANCZOS)
    Image.merge("LA", (Image.new("L", a.size, 0), a)).save(dst, optimize=True)
    print(f"  {dst.relative_to(ROOT)}  {width}x{h}  {dst.stat().st_size // 1024}KB")


def plate(alpha: Image.Image, size: int, bg: tuple, fg: tuple, pad=0.18) -> Image.Image:
    """둥근 사각 판 위에 마크. 판이 불투명해야 탭에서 사라지지 않는다."""
    card = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, size - 1, size - 1], radius=round(size * 0.22), fill=255
    )
    card.paste(Image.new("RGBA", (size, size), bg + (255,)), (0, 0), mask)

    inner = round(size * (1 - pad * 2))
    w, h = alpha.size
    w2, h2 = (inner, max(1, round(h * inner / w))) if w >= h else (max(1, round(w * inner / h)), inner)
    a = alpha.resize((w2, h2), Image.LANCZOS)
    layer = Image.new("RGBA", (w2, h2), fg + (255,))
    layer.putalpha(a)
    card.paste(layer, ((size - w2) // 2, (size - h2) // 2), layer)
    return card


def main() -> int:
    IMG.mkdir(parents=True, exist_ok=True)
    (IMG / "projects").mkdir(exist_ok=True)

    sqzer = shape(SRC_DIR / "sqzer_logo.png")
    write_mask(sqzer, IMG / "mark.png", 128)
    write_mask(shape(SRC_DIR / "sqzass_logo.png"), IMG / "projects" / "sqzass.png", 400)

    # 밝은 탭 → 검은 판, 어두운 탭 → 흰 판. 어느 쪽에서도 대비가 남는다.
    plate(sqzer, 64, INK, PAPER).save(IMG / "favicon.png", optimize=True)
    plate(sqzer, 64, PAPER, INK).save(IMG / "favicon-dark.png", optimize=True)
    plate(sqzer, 180, INK, PAPER).convert("RGB").save(IMG / "apple-touch-icon.png", optimize=True)
    for f in ("favicon.png", "favicon-dark.png", "apple-touch-icon.png"):
        print(f"  images/{f}  {(IMG / f).stat().st_size}B")
    return 0


if __name__ == "__main__":
    sys.exit(main())
