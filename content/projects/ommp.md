+++
title = "ommp"
description = "A standalone terminal music player built with Rust. No MPD, no daemon."
weight = 20
date = 2026-08-01

[extra]
tier = "landing"

eyebrow  = "Terminal music player · Rust"
tagline  = "Most terminal music players are a client for something else you have to start first. ommp is the whole thing: run it, and it plays. Quit it, and nothing is left running."
lang     = "Rust"
license  = "Apache-2.0"
version  = ""
platform = "Linux"
repo     = "https://github.com/sqzer-x/ommp"
stars     = 0
mark     = ""
logo     = ""

actions = [
  { label = "Website", url = "https://ommp.sqzer.com",            style = "primary" },
  { label = "Source",  url = "https://github.com/sqzer-x/ommp",   style = "ghost"   },
]

facts = [
  { value = "8",           label = "Audio formats" },
  { value = "3",           label = "Image protocols" },
  { value = "0",           label = "Daemons to start" },
  { value = "Apache-2.0",  label = "License" },
]

features_eyebrow = "Capabilities"
features_title   = "A library browser, a queue, and the artwork"
features_intro   = "Three panels. The left browses, the centre queues, the right shows the cover and the track."
# 항목은 아래 [[extra.features]] 에 있다. 인라인 테이블은 TOML 1.0 에서
# 한 줄을 넘지 못하고, 이 설명들은 한 줄에 들어가지 않는다.

session_eyebrow = "Install"
session_title   = "One command, then your music"
session_shell   = "zsh"
session_caption = "Needs a Nerd Font for the interface icons and a true-colour terminal."
session_lines = [
  { kind = "cmd",     text = "$ cargo install ommp" },
  { kind = "comment", text = "# on Arch:  yay -S ommp" },
  { kind = "cmd",     text = "$ ommp" },
  { kind = "comment", text = "# reads ~/Music, scans subdirectories, picks up changes as they happen" },
  { kind = "out",     text = "  Ctrl+S   search      artist:  album:  genre:  *.flac" },
  { kind = "out",     text = "  Ctrl+H   keybindings" },
]

cta_title = "Put your music in ~/Music and run it."
cta_text  = "Nothing to configure. Album art comes out of the tags in the files themselves."
cta_actions = [
  { label = "ommp.sqzer.com", url = "https://ommp.sqzer.com",          style = "primary" },
  { label = "Source",         url = "https://github.com/sqzer-x/ommp", style = "ghost"   },
]

[[extra.features]]
title = "Eight formats"
desc  = "FLAC, MP3, M4A, OGG, WAV, Opus, AAC and WMA, through PulseAudio or ALSA."

[[extra.features]]
title = "Album art, actually drawn"
desc  = "Kitty graphics, Sixel or the iTerm2 protocol, detected at startup. Everywhere else it falls back to block characters, which still shows the cover."

[[extra.features]]
title = "Browse how you think"
desc  = "By artist, album, genre, format, directory or playlist. The tabs across the top switch the left panel."

[[extra.features]]
title = "Field search"
desc  = "Ctrl+S filters as you type. artist:radiohead, album:ok computer, genre:rock, or *.flac."

[[extra.features]]
title = "It remembers"
desc  = "Volume, playlists and pane layout survive a restart, and the library re-syncs when files appear or vanish."

[[extra.features]]
title = "Mouse, if you want it"
desc  = "Click, scroll, and drag the panes to resize. The keyboard does everything too — Ctrl+H lists the bindings."

+++

Album art is read from the tags in the audio files, so there is nothing to place
alongside them. Which drawing protocol your terminal supports is worked out at
startup — Ghostty, Kitty, WezTerm and Konsole get real images; foot and xterm
built with Sixel do too.
