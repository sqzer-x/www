+++
title = "ommp"
description = "A standalone terminal music player built with Rust. No MPD, no daemon."
weight = 20
date = 2026-08-01

[extra]
tier = "landing"

eyebrow = "Terminal music player · Rust"
tagline = "Most terminal music players are a client for something else you have to start first. ommp is the whole thing: run it, and it plays. Quit it, and nothing is left running."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/ommp"
stars = 0

accent = "#7fc0d4"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "Website", url = "https://ommp.sqzer.com", style = "primary" },
  { label = "Source", url = "https://github.com/sqzer-x/ommp", style = "ghost" },
]

# 결정 목록의 머리. 항목은 아래 [[extra.register]] 에 있다.
register_eyebrow = "Capabilities"
register_title   = "A library browser, a queue, and the artwork"
register_intro   = "Three panels. The left browses, the centre queues, the right shows the cover and the track."

# 닫는 줄. 제목도 띠도 두 번째 버튼 줄도 없다 — 한 문장과 갈 곳뿐이다.
closing_text  = "Put your music in ~/Music and run it. There is nothing to configure — album art comes out of the tags in the files themselves."
closing_links = [
  { label = "ommp.sqzer.com", url = "https://ommp.sqzer.com" },
]

# ---- 스펙. 배지 줄과 큰 숫자 띠를 대신한다. 순서가 곧 화면 순서다.
# 키는 라벨이라 두 언어에서 영어다. url 이 비면 링크가 아니라 글자다.

[[extra.spec]]
key = "Language"
value = "Rust"
url = ""

[[extra.spec]]
key = "License"
value = "Apache-2.0"
url = ""

[[extra.spec]]
key = "Platform"
value = "Linux"
url = ""

[[extra.spec]]
key = "Audio formats"
value = "FLAC · MP3 · M4A · OGG · WAV · Opus · AAC · WMA"
url = ""

[[extra.spec]]
key = "Image protocols"
value = "Kitty · Sixel · iTerm2"
url = ""

[[extra.spec]]
key = "Daemons to start"
value = "0"
url = ""

# ---- 세션. 주장 하나에 영수증 하나. 여러 개일 수 있다.

[[extra.session]]
eyebrow = "Install"
title   = "One command, then your music"
caption = "Needs a Nerd Font for the interface icons and a true-colour terminal."
lines = [
  { kind = "cmd", text = "$ cargo install ommp" },
  { kind = "comment", text = "# on Arch:  yay -S ommp" },
  { kind = "cmd", text = "$ ommp" },
  { kind = "comment", text = "# reads ~/Music, scans subdirectories, picks up changes as they happen" },
  { kind = "out", text = "  Ctrl+S   search      artist:  album:  genre:  *.flac" },
  { kind = "out", text = "  Ctrl+H   keybindings" },
]

# ---- 결정. 번호는 저자가 적지 않는다. 순서가 곧 번호다.

[[extra.register]]
title = "Eight formats"
body  = "FLAC, MP3, M4A, OGG, WAV, Opus, AAC and WMA, through PulseAudio or ALSA."

[[extra.register]]
title = "Album art, actually drawn"
body  = "Kitty graphics, Sixel or the iTerm2 protocol, detected at startup. Everywhere else it falls back to block characters, which still shows the cover."

[[extra.register]]
title = "Browse how you think"
body  = "By artist, album, genre, format, directory or playlist. The tabs across the top switch the left panel."

[[extra.register]]
title = "Field search"
body  = "Ctrl+S filters as you type. artist:radiohead, album:ok computer, genre:rock, or *.flac."

[[extra.register]]
title = "It remembers"
body  = "Volume, playlists and pane layout survive a restart, and the library re-syncs when files appear or vanish."

[[extra.register]]
title = "Mouse, if you want it"
body  = "Click, scroll, and drag the panes to resize. The keyboard does everything too — Ctrl+H lists the bindings."

+++

Album art is read from the tags in the audio files, so there is nothing to place
alongside them. Which drawing protocol your terminal supports is worked out at
startup — Ghostty, Kitty, WezTerm and Konsole get real images; foot and xterm
built with Sixel do too.
