+++
title = "udfx"
description = "Ultimate Domain Finder X. Pulls every DNS record out of Active Directory over LDAP."
weight = 40
date = 2026-02-06

[extra]
tier = "brief"

eyebrow = "Active Directory DNS · PowerShell"
tagline = "In an air-gapped Windows estate the DNS zone is the map, and Active Directory is already holding it. This asks for it directly."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/udfx"
stars = 0

accent = "#c2a06e"
mark   = ""
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "Source", url = "https://github.com/sqzer-x/udfx", style = "ghost" },
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
value = "Domain user"
url = ""

[[extra.spec]]
key = "Output files"
value = "4"
url = ""

+++

Every domain and subdomain registered in AD-integrated DNS, read over LDAP. No
internet, no extra service, and no administrator account — a plain domain user
is enough, which is the point: this is what an attacker who has one already
sees.

Each record comes out with its type (A, NS, CNAME, MX, SRV, TXT), its value, its
zone, and the root domain it belongs to, with zones sorted into primary,
subdomain and external. The run writes four files: the full record set as CSV,
JSON and text, plus a deduplicated list of root domains, which is usually the
one you actually open first.

```powershell
.\Get-ADDnsRecords.ps1 -Domain corp.example.com
```

Needs PowerShell 5.1 or newer on a domain-joined system.
