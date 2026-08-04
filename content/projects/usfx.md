+++
title = "usfx"
description = "Ultimate Subdomain Finder X. Twelve enumeration modules, none of which phone home."
weight = 50
date = 2026-01-20

[extra]
tier = "brief"

eyebrow = "Subdomain discovery · Python"
tagline = "Every well-known subdomain tool starts by querying a service on the internet. On an internal network that is exactly the thing you do not have."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/usfx"
stars = 1

accent = "#8fb9a2"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "Source", url = "https://github.com/sqzer-x/usfx", style = "ghost" },
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
value = "Cross-platform"
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

Point it at an internal DNS server and it works from there. Twelve techniques,
all of them offline:

DNS brute force · zone transfer (AXFR) · DNSSEC walking over NSEC and NSEC3 ·
record mining across MX, NS, TXT, SRV, SOA and CAA · reverse DNS sweep · CNAME
chain analysis · subdomain permutation · recursive sub-subdomain enumeration ·
virtual host discovery · TLS certificate SAN extraction · subdomain takeover
detection · web technology detection.

Three wordlists ship with it — roughly 500, 3,500 and 18,000 entries — and the
output has pipeline modes (`subs`, `web`, `ips`, `json`) so it chains into
whatever runs next instead of being parsed out of a report.

```bash
pip install usfx
```
