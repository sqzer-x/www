+++
title = "doomsday"
description = "챙겨야 할 날짜를 세어 주는 GNOME 셸 확장."
weight = 60
date = 2026-02-09

[extra]
tier = "brief"

eyebrow  = "GNOME 셸 확장 · JavaScript"
tagline  = "카운트다운은 이미 눈이 가는 자리에 있어야 쓸모가 있다. 이건 상단 패널, 시계 옆에 산다."
lang     = "JavaScript"
license  = "GPL-3.0"
version  = ""
platform = "GNOME 45 · 46 · 47"
logo     = ""

actions = [
  { label = "소스", url = "https://github.com/sqzer-x/doomsday", style = "ghost" },
]

facts = [
  { value = "45–47",   label = "GNOME" },
  { value = "∞",       label = "이벤트" },
  { value = "자정",     label = "갱신" },
  { value = "GPL-3.0", label = "라이선스" },
]

features_eyebrow = ""
features_title   = ""
features_intro   = ""
features = []

session_eyebrow = ""
session_title   = ""
session_shell   = ""
session_caption = ""
session_lines = []

cta_title = ""
cta_text  = ""
cta_actions = []
+++

GNOME 상단 패널에 D-Day 를 띄운다. 이벤트는 원하는 만큼 넣고, 한 번 눌러서
바꾸고, 설정 창을 열지 않고 확장 메뉴에서 바로 고치거나 지운다. 쓰는 물건과 한 번
설정하고 잊는 물건의 차이가 거기서 갈린다.

날짜는 자정에 넘어가고, 패널에서의 자리는 왼쪽·가운데·오른쪽 중에 고른다.

Extension Manager 로 배포된 zip 을 설치하거나, 레포를 받아서 `./install.sh` 를
실행하면 된다.
