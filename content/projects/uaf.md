+++
title = "uaf"
description = "Ultimate AP Finder. Wireless AP discovery and classification for PCI-DSS audits."
weight = 30
date = 2026-02-14

[extra]
tier = "brief"

eyebrow = "Wireless AP audit · Python"
tagline = "PCI-DSS asks for a wireless assessment, and the honest version of that question is: which of these access points are ours, and which of them are open?"

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/uaf"
stars = 0

accent = "#9aa6cc"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "Source", url = "https://github.com/sqzer-x/uaf", style = "ghost" },
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
value = "Python 3.10+"
url = ""

[[extra.spec]]
key = "Platform"
value = "Linux"
url = ""

[[extra.spec]]
key = "Bands"
value = "2.4 · 5 · 6 GHz"
url = ""

[[extra.spec]]
key = "Security classes"
value = "WEP · WPA · WPA2 · WPA3 · OPN"
url = ""

[[extra.spec]]
key = "Privileges"
value = "root"
url = ""

+++

Scanning tools tend to stop at a list of SSIDs. An audit report needs more than
that: whether the encryption is WEP or WPA3, whether the SSID is hidden, who
made the radio, and — for the open ones — what is actually behind them.

**Passive.** Real-time detection across 2.4, 5 and 6 GHz. Every AP is classified
by security (WEP, WPA, WPA2, WPA3, OPN) and by standard (802.11 a/b/g/n/ac/ax),
with channel width, hidden-SSID recovery and MAC vendor lookup. Open networks
are highlighted, because those are the ones the report is about.

**Active.** Pick a suspicious open AP from the list and uaf connects to it, then
maps what it finds: DHCP details, an ARP sweep for other clients, and a port
scan of the gateway. Results come back in an overlay rather than a new screen.

**Export.** CSV and JSON, active-scan results included, so the findings go
straight into the audit document instead of being retyped.

Needs a Linux box with `iw` and `ip`, root, and an adapter that does monitor
mode.

```bash
pip install uaf
```
