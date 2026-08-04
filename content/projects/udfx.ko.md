+++
title = "udfx"
description = "Ultimate Domain Finder X. Active Directory 의 DNS 레코드를 LDAP 으로 전부 끌어온다."
weight = 40
date = 2026-02-06

[extra]
tier = "brief"

eyebrow = "Active Directory DNS · PowerShell"
tagline = "망이 끊긴 윈도우 환경에서 DNS 영역이 곧 지도이고, 그 지도는 이미 Active Directory 가 들고 있다. 이 도구는 그걸 직접 달라고 한다."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/udfx"
stars = 0

accent = "#c2a06e"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "소스", url = "https://github.com/sqzer-x/udfx", style = "ghost" },
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
value = "PowerShell 5.1+"
url = ""

[[extra.spec]]
key = "Platform"
value = "Windows"
url = ""

[[extra.spec]]
key = "Method"
value = "LDAP"
url = ""

[[extra.spec]]
key = "Privileges"
value = "도메인 사용자"
url = ""

[[extra.spec]]
key = "Output files"
value = "4"
url = ""

+++

AD 통합 DNS 에 등록된 모든 도메인과 서브도메인을 LDAP 으로 읽는다. 인터넷도,
별도 서비스도, 관리자 계정도 필요 없다. 평범한 도메인 사용자면 충분하다는 것이
핵심이다. 계정 하나를 이미 쥔 공격자가 보는 것이 정확히 이 화면이다.

레코드마다 타입(A, NS, CNAME, MX, SRV, TXT), 값, 영역, 그리고 속한 루트 도메인이
함께 나오고, 영역은 primary 와 subdomain 과 external 로 갈라진다. 한 번 돌리면
파일 네 개가 생긴다. 전체 레코드를 CSV 와 JSON 과 텍스트로, 그리고 중복을 없앤
루트 도메인 목록 하나. 실제로 먼저 여는 것은 보통 마지막 파일이다.

```powershell
.\Get-ADDnsRecords.ps1 -Domain corp.example.com
```

도메인에 가입된 시스템에서 PowerShell 5.1 이상이 필요하다.
