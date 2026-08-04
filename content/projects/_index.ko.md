+++
title = "프로젝트"
description = "터미널 소프트웨어, 보안 도구, 그리고 데스크톱 확장."
weight = 20
template = "projects.html"
page_template = "project.html"

# 카탈로그. 목록은 title·description·url·weight·date 만 실어 오므로 언어 배지와
# 링크는 여기 있어야 한다. url 은 한국어 트리를 가리켜야 한다.
[extra]

# 인라인 테이블은 TOML 1.0 에서 한 줄을 넘지 못한다. Rust 쪽 파서는 넘겨 주지만
# 그건 확장이고, 파서를 바꾸는 날 깨진다.
[[extra.featured]]
url   = "/ko/projects/sqzass/"
name  = "sqzass"
lang  = "Rust"
mark  = "images/projects/sqzass.png"
cover = ""
blurb = "깨진 참조를 발행하지 않는 정적 사이트 생성기."
site  = "https://sqzass.sqzer.com"
repo  = "https://github.com/sqzer-x/sqzass"
stars  = 0

[[extra.featured]]
url   = "/ko/projects/ommp/"
name  = "ommp"
lang  = "Rust"
mark  = ""
cover = "images/projects/ommp-cover.png"
blurb = "띄워 둘 데몬도, 끄고 남는 것도 없는 터미널 음악 재생기."
site  = "https://ommp.sqzer.com"
repo  = "https://github.com/sqzer-x/ommp"
stars  = 0

[[extra.group]]
id = "security"
label = "보안 도구"
note = "내부망이 무언가를 숨겨 두는 층마다 하나씩. 셋 다 인터넷 없이 동작한다."

  [[extra.group.item]]
  url = "/ko/projects/uaf/"
  name = "uaf"
  blurb = "Ultimate AP Finder. PCI-DSS 감사를 위한 무선 AP 탐지와 분류."
  mark = ""
  lang = "Python"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/uaf"
  stars = 0

  [[extra.group.item]]
  url = "/ko/projects/udfx/"
  name = "udfx"
  blurb = "Ultimate Domain Finder X. Active Directory 의 DNS 레코드를 LDAP 으로 전부 끌어온다."
  mark = ""
  lang = "PowerShell"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/udfx"
  stars = 0

  [[extra.group.item]]
  url = "/ko/projects/usfx/"
  name = "usfx"
  blurb = "Ultimate Subdomain Finder X. 열두 가지 열거 기법, 전부 외부를 부르지 않는다."
  mark = ""
  lang = "Python"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/usfx"
  stars = 1

[[extra.group]]
id = "apps"
label = "앱"
note = ""

  [[extra.group.item]]
  url = "/ko/projects/doomsday/"
  name = "doomsday"
  blurb = "챙겨야 할 날짜를 세어 주는 GNOME 셸 확장."
  mark = ""
  lang = "JavaScript"
  status = "active"
  site = ""
  repo = "https://github.com/sqzer-x/doomsday"
  stars = 0
+++
