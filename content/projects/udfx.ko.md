+++
title = "udfx"
description = "Ultimate Domain Finder X. Active Directory 의 DNS 레코드를 LDAP 으로 전부 끌어온다."
weight = 40
date = 2026-02-06

[extra]
tier = "brief"

eyebrow  = "Active Directory DNS · PowerShell"
tagline  = "망이 끊긴 윈도우 환경에서 DNS 영역이 곧 지도이고, 그 지도는 이미 Active Directory 가 들고 있다. 이 도구는 그걸 직접 달라고 한다."
lang     = "PowerShell"
license  = ""
version  = ""
platform = "Windows"
repo     = "https://github.com/sqzer-x/udfx"
stars     = 0
accent     = "#c2a06e"
mark     = ""
logo     = ""

actions = [
  { label = "소스", url = "https://github.com/sqzer-x/udfx", style = "ghost" },
]

facts = [
  { value = "LDAP",        label = "조회 방식" },
  { value = "5.1+",        label = "PowerShell" },
  { value = "도메인 사용자", label = "권한" },
  { value = "4",           label = "출력 파일" },
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
