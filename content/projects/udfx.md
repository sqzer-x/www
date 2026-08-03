+++
title = "udfx"
description = "Ultimate Domain Finder X. Pulls every DNS record out of Active Directory over LDAP."
weight = 40
date = 2026-02-06

[extra]
tier = "brief"

eyebrow  = "Active Directory DNS · PowerShell"
tagline  = "In an air-gapped Windows estate the DNS zone is the map, and Active Directory is already holding it. This asks for it directly."
lang     = "PowerShell"
license  = ""
version  = ""
platform = "Windows"
logo     = ""

actions = [
  { label = "Source", url = "https://github.com/sqzer-x/udfx", style = "ghost" },
]

facts = [
  { value = "LDAP",        label = "Method" },
  { value = "5.1+",        label = "PowerShell" },
  { value = "Domain user", label = "Privileges" },
  { value = "4",           label = "Output files" },
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
