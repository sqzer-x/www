+++
title = "usfx"
description = "Ultimate Subdomain Finder X. 열두 가지 열거 기법, 전부 외부를 부르지 않는다."
weight = 50
date = 2026-01-20

[extra]
tier = "brief"

eyebrow  = "서브도메인 탐색 · Python"
tagline  = "이름난 서브도메인 도구는 하나같이 인터넷의 어떤 서비스를 부르는 것으로 시작한다. 내부망에서는 그게 정확히 없는 것이다."
lang     = "Python"
license  = ""
version  = "1.2.0"
platform = "크로스 플랫폼"
repo     = "https://github.com/sqzer-x/usfx"
stars     = 1
mark     = ""
logo     = ""

actions = [
  { label = "소스", url = "https://github.com/sqzer-x/usfx", style = "ghost" },
]

facts = [
  { value = "12",     label = "모듈" },
  { value = "18,000", label = "최대 워드리스트" },
  { value = "0",      label = "외부 서비스" },
  { value = "1.2.0",  label = "버전" },
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
