+++
title = "usfx"
description = "Ultimate Subdomain Finder X. Twelve enumeration modules, none of which phone home."
weight = 50
date = 2026-01-20

[extra]
tier = "brief"

eyebrow  = "Subdomain discovery · Python"
tagline  = "Every well-known subdomain tool starts by querying a service on the internet. On an internal network that is exactly the thing you do not have."
lang     = "Python"
license  = ""
version  = "1.2.0"
platform = "Cross-platform"
logo     = ""

actions = [
  { label = "Source", url = "https://github.com/sqzer-x/usfx", style = "ghost" },
]

facts = [
  { value = "12",     label = "Modules" },
  { value = "18,000", label = "Largest wordlist" },
  { value = "0",      label = "External services" },
  { value = "1.2.0",  label = "Version" },
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
