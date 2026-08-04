+++
title = "uaf"
description = "Ultimate AP Finder. PCI-DSS 감사를 위한 무선 AP 탐지와 분류."
weight = 30
date = 2026-02-14

[extra]
tier = "brief"

eyebrow = "무선 AP 감사 · Python"
tagline = "PCI-DSS 는 무선 점검을 요구한다. 그 요구를 솔직하게 옮기면 이런 질문이 된다. 이 AP 들 중 어느 것이 우리 것이고, 어느 것이 열려 있는가."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/uaf"
stars = 0

accent = "#9aa6cc"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "소스", url = "https://github.com/sqzer-x/uaf", style = "ghost" },
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

스캔 도구는 대개 SSID 목록에서 멈춘다. 감사 보고서에는 그것만으로 부족하다.
암호화가 WEP 인지 WPA3 인지, SSID 를 숨겼는지, 무선 칩을 누가 만들었는지, 그리고
열려 있는 것들 뒤에는 실제로 무엇이 있는지가 필요하다.

**수동 스캔.** 2.4, 5, 6 GHz 를 실시간으로 훑는다. 모든 AP 를 보안(WEP, WPA,
WPA2, WPA3, OPN)과 규격(802.11 a/b/g/n/ac/ax)으로 분류하고, 채널 폭과 숨긴 SSID
복원과 MAC 제조사 조회까지 붙인다. 열린 네트워크는 눈에 띄게 표시한다. 보고서가
말하려는 것이 그것이기 때문이다.

**능동 스캔.** 목록에서 의심스러운 개방 AP 를 고르면 접속한 뒤 구조를 그린다.
DHCP 정보, 다른 단말을 찾는 ARP 스윕, 게이트웨이 포트 스캔. 결과는 화면을 옮기지
않고 겹쳐 띄운다.

**내보내기.** 능동 스캔 결과까지 포함해 CSV 와 JSON 으로 낸다. 옮겨 적는 대신
그대로 감사 문서에 들어간다.

`iw` 와 `ip` 가 있는 Linux, root 권한, 모니터 모드가 되는 어댑터가 필요하다.

```bash
pip install uaf
```
