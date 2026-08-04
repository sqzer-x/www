+++
title = "doomsday"
description = "A GNOME Shell extension that counts down to the dates you care about."
weight = 60
date = 2026-02-09

[extra]
tier = "brief"

eyebrow = "GNOME Shell extension · JavaScript"
tagline = "A countdown is only useful where you already look. This one lives in the top panel, next to the clock."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/doomsday"
stars = 0

accent = "#c98a8a"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "Source", url = "https://github.com/sqzer-x/doomsday", style = "ghost" },
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
value = "Daily, at midnight"
url = ""

+++

D-Day counters in the GNOME top panel. Add as many events as you like, switch
between them with one click, and edit or delete them from the extension menu
without opening preferences — which is the difference between a thing you use
and a thing you configure once and forget.

The count rolls over at midnight, and the panel position is yours to pick: left,
centre or right.

Install through Extension Manager with the packaged zip, or clone the repository
and run `./install.sh`.
