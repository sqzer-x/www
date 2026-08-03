+++
title = "Projects"
description = "Open-source terminal software, security tooling, and a desktop extension."
weight = 20
template = "projects.html"
page_template = "project.html"

# 카탈로그. 목록(PageRefCtx)은 title·description·url·weight·date 만 실어 오므로
# 언어 배지와 링크는 여기 있어야 한다.
#
# 모든 url 은 content/projects/ 아래 실제 페이지를 가리켜야 한다. [extra] 안의
# URL 은 빌드가 확인해 주지 않는 유일한 참조라, 그 대응은 CI 가 검사한다.
#
# 스키마는 총체적이다. 없는 값은 "" 이고 키를 빼지 않는다 — 정의되지 않은 접근은
# 빌드 에러라 키 하나가 빠지면 사이트 전체가 안 나온다.
[extra]

# 큰 카드. 자기 랜딩 페이지를 가진 둘.
#
# 인라인 테이블을 쓰지 않는 이유: TOML 1.0 에서 인라인 테이블은 한 줄을 넘지
# 못한다. Rust 쪽 파서는 넘겨 주지만 그건 확장이고, 파서를 바꾸는 날 깨진다.
[[extra.featured]]
url   = "/projects/sqzass/"
name  = "sqzass"
lang  = "Rust"
cover = ""
blurb = "A static site generator that refuses to publish a broken reference."
site  = "https://sqzass.sqzer.com"
repo  = "https://github.com/sqzer-x/sqzass"

[[extra.featured]]
url   = "/projects/ommp/"
name  = "ommp"
lang  = "Rust"
cover = ""
blurb = "A terminal music player with no daemon to start and nothing left running."
site  = "https://ommp.sqzer.com"
repo  = "https://github.com/sqzer-x/ommp"

[[extra.group]]
id = "terminal"
label = "Terminal tools"
note = ""

  [[extra.group.item]]
  url = "/projects/sqzass/"
  name = "sqzass"
  blurb = "Static site generator. Two builds of the same input are byte-identical."
  lang = "Rust"
  status = "active"
  site = "https://sqzass.sqzer.com"
  repo = "https://github.com/sqzer-x/sqzass"

  [[extra.group.item]]
  url = "/projects/ommp/"
  name = "ommp"
  blurb = "Terminal music player. No MPD, no daemon — run it and play."
  lang = "Rust"
  status = "active"
  site = "https://ommp.sqzer.com"
  repo = "https://github.com/sqzer-x/ommp"

# uaf / udfx / usfx 는 이름이 우연히 닮은 것이 아니다. 정찰 대상이 AP, 도메인,
# 서브도메인으로 갈라지는 한 계열이고, 셋 다 인터넷이 없는 망에서 도는 것을
# 전제로 만들어졌다. 그래서 한 갈래로 묶는다.
[[extra.group]]
id = "security"
label = "Security tools"
note = "Three finders, one for each layer an internal network hides things at. All of them work with no internet connection."

  [[extra.group.item]]
  url = "/projects/uaf/"
  name = "uaf"
  blurb = "Ultimate AP Finder. Wireless AP discovery and classification for PCI-DSS audits."
  lang = "Python"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/uaf"

  [[extra.group.item]]
  url = "/projects/udfx/"
  name = "udfx"
  blurb = "Ultimate Domain Finder X. Pulls every DNS record out of Active Directory over LDAP."
  lang = "PowerShell"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/udfx"

  [[extra.group.item]]
  url = "/projects/usfx/"
  name = "usfx"
  blurb = "Ultimate Subdomain Finder X. Twelve enumeration modules, none of which phone home."
  lang = "Python"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/usfx"

[[extra.group]]
id = "apps"
label = "Apps"
note = ""

  [[extra.group.item]]
  url = "/projects/doomsday/"
  name = "doomsday"
  blurb = "A GNOME Shell extension that counts down to the dates you care about."
  lang = "JavaScript"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/doomsday"
+++
