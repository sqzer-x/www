+++
title = "sqzass"
description = "A static site generator written in Rust. This site is built with it."
weight = 10
date = 2026-07-31

[extra]
tier = "landing"

eyebrow = "Static site generator · Rust"
tagline = "Most generators lean on their host for pretty URLs, redirects and cache headers. sqzass does that work itself, so the same output is correct on GitHub Pages, on Vercel, or in a directory served over plain HTTP."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/sqzass"
stars = 0

accent = "#e0a06a"
mark   = "images/projects/sqzass.png"
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "Documentation", url = "https://sqzass.sqzer.com", style = "primary" },
  { label = "Source", url = "https://github.com/sqzer-x/sqzass", style = "ghost" },
]

# 결정 목록의 머리. 항목은 아래 [[extra.register]] 에 있다.
register_eyebrow = "Design"
register_title   = "Six decisions, and the argument for each"
register_intro   = "None of these are preferences. Each one is a failure that happened somewhere else first."

# 닫는 줄. 제목도 띠도 두 번째 버튼 줄도 없다 — 한 문장과 갈 곳뿐이다.
closing_text  = "Start with the quickstart in the documentation. The rest of it is reference, and it is written in the same two languages this site is."
closing_links = [
  { label = "sqzass.sqzer.com", url = "https://sqzass.sqzer.com" },
]

# ---- 스펙. 배지 줄과 큰 숫자 띠를 대신한다. 순서가 곧 화면 순서다.
# 키는 라벨이라 두 언어에서 영어다. url 이 비면 링크가 아니라 글자다.

[[extra.spec]]
key = "Language"
value = "Rust"
url = ""

[[extra.spec]]
key = "License"
value = "MIT"
url = ""

[[extra.spec]]
key = "Version"
value = "0.1.0"
url = ""

[[extra.spec]]
key = "Platform"
value = "Linux · macOS"
url = ""

[[extra.spec]]
key = "Build"
value = "25 ms for 1,000 pages"
url = ""

[[extra.spec]]
key = "Runtime dependencies"
value = "0"
url = ""

# ---- 세션. 주장 하나에 영수증 하나. 여러 개일 수 있다.

[[extra.session]]
eyebrow = "Quickstart"
title   = "Three files, then a site"
caption = "Real output. The documentation site in this repository is 60 pages."
lines = [
  { kind = "cmd", text = "$ sqzass init mysite" },
  { kind = "comment", text = "# writes sqzass.toml, content/_index.md, templates/page.html" },
  { kind = "cmd", text = "$ sqzass serve -i mysite" },
  { kind = "out", text = "  http://127.0.0.1:3000   live reload" },
  { kind = "cmd", text = "$ sqzass build -i docs" },
  { kind = "out", text = "  60 pages → docs/public" },
]

# ---- 결정. 번호는 저자가 적지 않는다. 순서가 곧 번호다.

[[extra.register]]
title = "Broken references stop the build"
body  = "An unresolved link, a missing template, two pages claiming the same URL, a misspelled config key — every one is an error, not a warning you scroll past."

[[extra.register]]
title = "Markdown on the AST"
body  = "Link rewriting, heading anchors and the table of contents are tree operations. A regex over finished HTML silently skips any attribute that is single-quoted."

[[extra.register]]
title = "Byte-identical builds"
body  = "Two builds of the same input produce the same bytes, and CI checks it on every push. Rendering is parallel; determinism comes from the merge, not the schedule."

[[extra.register]]
title = "Korean was not bolted on"
body  = "Translations sit beside their originals, links resolve to the reader's language, and search matches substrings — the only way 최적화 inside 검색엔진최적화 is ever found."

[[extra.register]]
title = "Classes, never inline styles"
body  = "Highlighting emits class names. Inline colours pin one theme into every document forever and put a strict style-src out of reach."

[[extra.register]]
title = "One binary, no runtime"
body  = "No Node, no Python, no system libraries. The thing you download is the thing that runs."

+++

The site you are reading is built with it. So is [its own documentation][docs] —
which makes the docs a regression test for the generator, since CI builds them
with the binary it just compiled.

[docs]: https://sqzass.sqzer.com
