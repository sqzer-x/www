+++
title = "Home"
description = "Terminal tools, static site tooling, and offensive security utilities."
template = "home.html"

# 카피는 전부 여기 있고 템플릿은 구조만 안다. 두 언어가 같은 키를 1:1 로 갖는다.
[extra]
hero_title = "Software Engineer, Security Engineer and Founder"
hero_sub   = "Hello! I'm An Hyukjin, though I go by various aliases online (protect your OPSEC!). I'm a Software & Security Engineer based in South Korea."
hero_door  = "About me"

# 맨 위 글의 미리보기. 목록이 실어 오는 것은 title·description·url·weight·date 뿐이라
# (PageRefCtx 에는 extra 가 없다) 영상 경로가 거기서 나올 수 없다. Projects 카탈로그가
# [extra] 에 사는 것과 같은 이유이고, url 이 실제 페이지를 가리키는지는 CI 가 검사한다.
#
# 여기 없는 글은 그냥 미리보기가 없다. 새 글이 맨 위에 올라와도 페이지는 멀쩡하고,
# 영상이 있는 글이면 이 줄을 고치면 된다.
# 홈의 프로젝트 모자이크. 목록(PageRefCtx)에 extra 가 없어서 그림과 색은 여기
# 있어야 한다. 여기 있는 것은 **그림과 색과 순서**뿐이다 — 이름과 설명은 목록이
# 실어 오므로 두 곳이 어긋날 수 없다.
#
# 첫 항목이 큰 타일이다. 넷만 싣는다; 나머지는 문이 받는다.
# cover 가 있으면 그 그림이 꽉 찬다. 없고 mark 만 있으면 그 마크가 프로젝트의
# 색 위에 앉는다. 둘 다 없으면 색만 남는다 — 그것도 그 프로젝트의 것이라
# "그림 없음" 판보다 낫다.
[[extra.mosaic]]
url    = "/projects/sqzass/"
cover  = ""
mark   = "images/projects/sqzass.png"
accent = "#e0a06a"
repo   = "https://github.com/sqzer-x/sqzass"
stars  = 0

[[extra.mosaic]]
url    = "/projects/ommp/"
cover  = "images/projects/ommp-cover.png"
mark   = ""
accent = "#7fc0d4"
repo   = "https://github.com/sqzer-x/ommp"
stars  = 0

[[extra.mosaic]]
url    = "/projects/uaf/"
cover  = ""
mark   = ""
accent = "#9aa6cc"
repo   = "https://github.com/sqzer-x/uaf"
stars  = 0

[[extra.mosaic]]
url    = "/projects/usfx/"
cover  = ""
mark   = ""
accent = "#8fb9a2"
repo   = "https://github.com/sqzer-x/usfx"
stars  = 1

[[extra.preview]]
url    = "/posts/a-new-beginning/"
poster = "images/posts/a-new-beginning.webp"
video  = "video/a-new-beginning.mp4"
+++
