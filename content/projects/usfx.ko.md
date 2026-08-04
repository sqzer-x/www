+++
title = "usfx"
description = "Ultimate Subdomain Finder X. 열두 가지 열거 기법, 전부 외부를 부르지 않는다."
weight = 50
date = 2026-01-20

[extra]
tier = "brief"

eyebrow = "서브도메인 탐색 · Python"
tagline = "이름난 서브도메인 도구는 하나같이 인터넷의 어떤 서비스를 부르는 것으로 시작한다. 내부망에서는 그게 정확히 없는 것이다."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/usfx"
stars = 1

accent = "#8fb9a2"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "소스", url = "https://github.com/sqzer-x/usfx", style = "ghost" },
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
value = "Python"
url = ""

[[extra.spec]]
key = "Version"
value = "1.2.0"
url = ""

[[extra.spec]]
key = "Platform"
value = "크로스 플랫폼"
url = ""

[[extra.spec]]
key = "Modules"
value = "12"
url = ""

[[extra.spec]]
key = "Largest wordlist"
value = "18,000"
url = ""

[[extra.spec]]
key = "External services"
value = "0"
url = ""

+++

내부 DNS 서버를 알려 주면 거기서부터 시작한다. 기법은 열두 가지이고 전부
오프라인이다.

DNS 무차별 대입 · 영역 전송(AXFR) · NSEC 과 NSEC3 를 따라가는 DNSSEC 워킹 ·
MX, NS, TXT, SRV, SOA, CAA 레코드 수집 · 역방향 DNS 스윕 · CNAME 체인 분석 ·
서브도메인 순열 · 재귀 하위 서브도메인 열거 · 가상 호스트 탐색 · TLS 인증서 SAN
추출 · 서브도메인 탈취 탐지 · 웹 기술 탐지.

워드리스트는 셋이 함께 들어 있고 각각 약 500, 3,500, 18,000 개다. 출력에는
파이프라인 모드(`subs`, `web`, `ips`, `json`)가 있어서, 보고서를 파싱하는 대신
다음에 돌 도구로 그대로 이어진다.

```bash
pip install usfx
```
