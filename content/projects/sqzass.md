+++
title = "sqzass"
description = "A static site generator written in Rust. This site is built with it."
weight = 10
date = 2026-07-31

[extra]
tier = "landing"

eyebrow  = "Static site generator · Rust"
tagline  = "Most generators lean on their host for pretty URLs, redirects and cache headers. sqzass does that work itself, so the same output is correct on GitHub Pages, on Vercel, or in a directory served over plain HTTP."
lang     = "Rust"
license  = "MIT"
version  = "0.1.0"
platform = "Linux · macOS"
logo     = ""

actions = [
  { label = "Documentation", url = "https://sqzass.sqzer.com",                 style = "primary" },
  { label = "Source",        url = "https://github.com/sqzer-x/sqzass",        style = "ghost"   },
]

# 별 개수 대신 확인할 수 있는 사실. Rust 도구를 보러 온 사람이 실제로 궁금해하는 것들이다.
facts = [
  { value = "25 ms",  label = "1,000 pages" },
  { value = "0",      label = "Runtime deps" },
  { value = "0.1.0",  label = "Version" },
  { value = "MIT",    label = "License" },
]

features_eyebrow = "Design"
features_title   = "Six decisions, and the argument for each"
features_intro   = "None of these are preferences. Each one is a failure that happened somewhere else first."
# 항목은 아래 [[extra.features]] 에 있다. 인라인 테이블은 TOML 1.0 에서
# 한 줄을 넘지 못하고, 이 설명들은 한 줄에 들어가지 않는다.

session_eyebrow = "Quickstart"
session_title   = "Three files, then a site"
session_shell   = "zsh"
session_caption = "Real output. The documentation site in this repository is 60 pages."
session_lines = [
  { kind = "cmd",     text = "$ sqzass init mysite" },
  { kind = "comment", text = "# writes sqzass.toml, content/_index.md, templates/page.html" },
  { kind = "cmd",     text = "$ sqzass serve -i mysite" },
  { kind = "out",     text = "  http://127.0.0.1:3000   live reload" },
  { kind = "cmd",     text = "$ sqzass build -i docs" },
  { kind = "out",     text = "  60 pages → docs/public" },
]

cta_title = "Read the documentation."
cta_text  = "Built with sqzass, from the docs directory of the same repository. CI builds it with the binary it just compiled."
cta_actions = [
  { label = "sqzass.sqzer.com", url = "https://sqzass.sqzer.com",          style = "primary" },
  { label = "Source",           url = "https://github.com/sqzer-x/sqzass", style = "ghost"   },
]

[[extra.features]]
title = "Broken references stop the build"
desc  = "An unresolved link, a missing template, two pages claiming the same URL, a misspelled config key — every one is an error, not a warning you scroll past."

[[extra.features]]
title = "Markdown on the AST"
desc  = "Link rewriting, heading anchors and the table of contents are tree operations. A regex over finished HTML silently skips any attribute that is single-quoted."

[[extra.features]]
title = "Byte-identical builds"
desc  = "Two builds of the same input produce the same bytes, and CI checks it on every push. Rendering is parallel; determinism comes from the merge, not the schedule."

[[extra.features]]
title = "Korean was not bolted on"
desc  = "Translations sit beside their originals, links resolve to the reader's language, and search matches substrings — the only way 최적화 inside 검색엔진최적화 is ever found."

[[extra.features]]
title = "Classes, never inline styles"
desc  = "Highlighting emits class names. Inline colours pin one theme into every document forever and put a strict style-src out of reach."

[[extra.features]]
title = "One binary, no runtime"
desc  = "No Node, no Python, no system libraries. The thing you download is the thing that runs."

+++

The site you are reading is built with it. So is [its own documentation][docs] —
which makes the docs a regression test for the generator, since CI builds them
with the binary it just compiled.

[docs]: https://sqzass.sqzer.com
