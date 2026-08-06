+++
title = "uaf"
description = "Ultimate AP Finder. Wireless AP discovery and classification for PCI-DSS audits."
weight = 30
date = 2026-02-14

[extra]
tier = "brief"

eyebrow  = "Wireless AP audit · Python"
tagline  = "PCI-DSS asks for a wireless assessment, and the honest version of that question is: which of these access points are ours, and which of them are open?"
lang     = "Python"
license  = ""
version  = ""
platform = "Linux"
repo     = "https://github.com/sqzer-x/uaf"
stars    = 0
accent     = "#9aa6cc"
mark     = ""
logo     = ""

actions = [
  { label = "Source", url = "https://github.com/sqzer-x/uaf", style = "ghost" },
]

facts = [
  { value = "3",     label = "Bands scanned" },
  { value = "5",     label = "Security classes" },
  { value = "3.10+", label = "Python" },
  { value = "root",  label = "Privileges" },
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
