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
[[extra.preview]]
url    = "/posts/a-new-beginning/"
poster = "images/posts/a-new-beginning.webp"
video  = "video/a-new-beginning.mp4"
+++
