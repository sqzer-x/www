+++
title = "ommp"
description = "Rust 로 만든 터미널 음악 재생기. MPD 도 데몬도 없다."
weight = 20
date = 2026-08-01

[extra]
tier = "landing"

eyebrow  = "터미널 음악 재생기 · Rust"
tagline  = "터미널 음악 재생기는 대개 먼저 띄워 둬야 하는 무언가의 클라이언트다. ommp 는 그 전부다. 실행하면 재생되고, 끄면 남는 것이 없다."
lang     = "Rust"
license  = "Apache-2.0"
version  = ""
platform = "Linux"
repo     = "https://github.com/sqzer-x/ommp"
stars     = 0
mark     = ""
logo     = ""

actions = [
  { label = "웹사이트", url = "https://ommp.sqzer.com",          style = "primary" },
  { label = "소스",     url = "https://github.com/sqzer-x/ommp", style = "ghost"   },
]

facts = [
  { value = "8",           label = "오디오 형식" },
  { value = "3",           label = "이미지 프로토콜" },
  { value = "0",           label = "띄울 데몬" },
  { value = "Apache-2.0",  label = "라이선스" },
]

features_eyebrow = "기능"
features_title   = "라이브러리, 재생 목록, 그리고 앨범 아트"
features_intro   = "화면은 세 칸이다. 왼쪽이 훑고, 가운데가 줄을 세우고, 오른쪽이 표지와 지금 곡을 보여 준다."
# 항목은 아래 [[extra.features]] 에 있다. 인라인 테이블은 TOML 1.0 에서
# 한 줄을 넘지 못하고, 이 설명들은 한 줄에 들어가지 않는다.

session_eyebrow = "설치"
session_title   = "명령 하나, 그다음이 음악"
session_shell   = "zsh"
session_caption = "인터페이스 아이콘에 Nerd Font 가, 색에 24비트 지원 터미널이 필요하다."
session_lines = [
  { kind = "cmd",     text = "$ cargo install ommp" },
  { kind = "comment", text = "# Arch 라면:  yay -S ommp" },
  { kind = "cmd",     text = "$ ommp" },
  { kind = "comment", text = "# ~/Music 을 읽고 하위 디렉터리까지 훑는다. 바뀌면 바로 따라간다" },
  { kind = "out",     text = "  Ctrl+S   검색        artist:  album:  genre:  *.flac" },
  { kind = "out",     text = "  Ctrl+H   키 목록" },
]

cta_title = "~/Music 에 음악을 두고 실행하면 됩니다."
cta_text  = "설정할 것이 없다. 앨범 아트는 파일 안의 태그에서 나온다."
cta_actions = [
  { label = "ommp.sqzer.com", url = "https://ommp.sqzer.com",          style = "primary" },
  { label = "소스",           url = "https://github.com/sqzer-x/ommp", style = "ghost"   },
]

[[extra.features]]
title = "여덟 가지 형식"
desc  = "FLAC, MP3, M4A, OGG, WAV, Opus, AAC, WMA 를 PulseAudio 나 ALSA 로 낸다."

[[extra.features]]
title = "앨범 아트를 실제로 그린다"
desc  = "Kitty 그래픽, Sixel, iTerm2 프로토콜 중 되는 것을 시작할 때 알아서 고른다. 아무것도 없으면 블록 문자로 떨어지는데, 그래도 표지는 보인다."

[[extra.features]]
title = "생각하는 대로 훑는다"
desc  = "아티스트, 앨범, 장르, 형식, 디렉터리, 재생 목록. 위쪽 탭이 왼쪽 칸을 바꾼다."

[[extra.features]]
title = "필드 검색"
desc  = "Ctrl+S 를 누르면 치는 대로 걸러진다. artist:radiohead, album:ok computer, genre:rock, *.flac."

[[extra.features]]
title = "기억한다"
desc  = "음량과 재생 목록과 칸 배치가 다시 켜도 그대로고, 파일이 생기거나 사라지면 라이브러리가 따라간다."

[[extra.features]]
title = "마우스도 쓴다"
desc  = "누르고 굴리고 끌어서 칸 크기를 바꾼다. 키보드로도 전부 되고, Ctrl+H 가 목록을 보여 준다."

+++

앨범 아트는 음악 파일의 태그에서 읽으므로 옆에 따로 둘 것이 없다. 터미널이 어떤
그리기 프로토콜을 지원하는지는 시작할 때 알아낸다. Ghostty, Kitty, WezTerm,
Konsole 은 실제 이미지가 나오고, foot 과 Sixel 을 켜서 빌드한 xterm 도 그렇다.
