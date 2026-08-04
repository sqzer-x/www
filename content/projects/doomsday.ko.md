+++
title = "doomsday"
description = "챙겨야 할 날짜를 세어 주는 GNOME 셸 확장."
weight = 60
date = 2026-02-09

[extra]
tier = "brief"

eyebrow = "GNOME 셸 확장 · JavaScript"
tagline = "카운트다운은 이미 눈이 가는 자리에 있어야 쓸모가 있다. 이건 상단 패널, 시계 옆에 산다."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/doomsday"
stars = 0

accent = "#c98a8a"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "소스", url = "https://github.com/sqzer-x/doomsday", style = "ghost" },
]

# 브리프에는 세션도 결정 목록도 없다. 빈 배열이 이미 '없음'이라
# 플래그를 따로 두지 않는다 — 템플릿이 데이터를 보고 정한다.
register_eyebrow = ""
register_title   = ""
register_intro   = ""
register = []
session  = []

# 닫는 줄. 제목도 띠도 두 번째 버튼 줄도 없다 — 한 문장과 갈 곳뿐이다.
closing_text  = ""
closing_links = []

# ---- 스펙. 배지 줄과 큰 숫자 띠를 대신한다. 순서가 곧 화면 순서다.
# 키는 라벨이라 두 언어에서 영어다. url 이 비면 링크가 아니라 글자다.

[[extra.spec]]
key = "Language"
value = "JavaScript"
url = ""

[[extra.spec]]
key = "License"
value = "GPL-3.0"
url = ""

[[extra.spec]]
key = "Platform"
value = "GNOME 45 · 46 · 47"
url = ""

[[extra.spec]]
key = "Refreshes"
value = "매일 자정"
url = ""

+++

GNOME 상단 패널에 D-Day 를 띄운다. 이벤트는 원하는 만큼 넣고, 한 번 눌러서
바꾸고, 설정 창을 열지 않고 확장 메뉴에서 바로 고치거나 지운다. 쓰는 물건과 한 번
설정하고 잊는 물건의 차이가 거기서 갈린다.

날짜는 자정에 넘어가고, 패널에서의 자리는 왼쪽·가운데·오른쪽 중에 고른다.

Extension Manager 로 배포된 zip 을 설치하거나, 레포를 받아서 `./install.sh` 를
실행하면 된다.
