+++
title = "sqzass"
description = "Rust 로 만든 정적 사이트 생성기. 이 사이트가 그걸로 만들어졌다."
weight = 10
date = 2026-07-31

[extra]
tier = "landing"

eyebrow = "정적 사이트 생성기 · Rust"
tagline = "대부분의 생성기는 예쁜 URL 과 리다이렉트, 캐시 헤더를 호스트에 맡긴다. sqzass 는 그 일을 직접 한다. 그래서 같은 출력이 GitHub Pages 에서도, Vercel 에서도, 평범한 HTTP 로 디렉터리를 내주는 서버에서도 똑같이 맞다."

# 저장소와 별 줄은 template 이 이 두 값에서 만든다. tools/stars.py 가 고쳐
# 쓰는 것이 이 짝이라, 스펙 표에 손으로 적으면 조용히 낡는다. 0 이어도 낸다.
repo  = "https://github.com/sqzer-x/sqzass"
stars = 0

accent = "#e0a06a"
mark   = "images/projects/sqzass.png"
logo   = ""

# 페이지에 버튼은 이 한 쌍뿐이다. 머리에 한 번, 그게 전부다.
actions = [
  { label = "문서", url = "https://sqzass.sqzer.com", style = "primary" },
  { label = "소스", url = "https://github.com/sqzer-x/sqzass", style = "ghost" },
]

# 결정 목록의 머리. 항목은 아래 [[extra.register]] 에 있다.
register_eyebrow = "설계"
register_title   = "여섯 개의 결정과 각각의 근거"
register_intro   = "취향이 아니다. 하나하나가 다른 데서 먼저 일어난 사고다."

# 닫는 줄. 제목도 띠도 두 번째 버튼 줄도 없다 — 한 문장과 갈 곳뿐이다.
closing_text  = "문서의 빠른 시작부터 보면 된다. 나머지는 레퍼런스이고, 이 사이트와 같은 두 언어로 쓰여 있다."
closing_links = [
  { label = "sqzass.sqzer.com", url = "https://sqzass.sqzer.com" },
]

# ---- 스펙. 배지 줄과 큰 숫자 띠를 대신한다. 순서가 곧 화면 순서다.
# 키는 라벨이라 두 언어에서 영어다. url 이 비면 링크가 아니라 글자다.

[[extra.spec]]
key = "Language"
value = "Rust"
url = ""

[[extra.spec]]
key = "License"
value = "MIT"
url = ""

[[extra.spec]]
key = "Version"
value = "0.1.0"
url = ""

[[extra.spec]]
key = "Platform"
value = "Linux · macOS"
url = ""

[[extra.spec]]
key = "Build"
value = "1,000 페이지에 25 ms"
url = ""

[[extra.spec]]
key = "Runtime dependencies"
value = "0"
url = ""

# ---- 세션. 주장 하나에 영수증 하나. 여러 개일 수 있다.

[[extra.session]]
eyebrow = "빠른 시작"
title   = "파일 세 개, 그다음이 사이트"
caption = "실제 출력이다. 이 레포의 문서 사이트가 60 페이지다."
lines = [
  { kind = "cmd", text = "$ sqzass init mysite" },
  { kind = "comment", text = "# sqzass.toml, content/_index.md, templates/page.html 을 쓴다" },
  { kind = "cmd", text = "$ sqzass serve -i mysite" },
  { kind = "out", text = "  http://127.0.0.1:3000   라이브 리로드" },
  { kind = "cmd", text = "$ sqzass build -i docs" },
  { kind = "out", text = "  60 pages → docs/public" },
]

# ---- 결정. 번호는 저자가 적지 않는다. 순서가 곧 번호다.

[[extra.register]]
title = "깨진 참조는 빌드를 세운다"
body  = "풀리지 않는 링크, 없는 템플릿, 같은 URL 을 주장하는 두 페이지, 오타 난 설정 키. 전부 경고가 아니라 에러다."

[[extra.register]]
title = "마크다운은 AST 에서 다룬다"
body  = "링크 재작성, 제목 앵커, 목차가 전부 트리 연산이다. 완성된 HTML 에 정규식을 돌리면 작은따옴표로 감싼 속성을 조용히 건너뛴다."

[[extra.register]]
title = "바이트까지 같은 빌드"
body  = "같은 입력을 두 번 빌드하면 같은 바이트가 나오고, CI 가 푸시마다 확인한다. 렌더는 병렬이고, 결정성은 일정이 아니라 병합이 만든다."

[[extra.register]]
title = "한국어는 나중에 얹은 것이 아니다"
body  = "번역이 원문 옆에 있고, 링크는 읽는 사람의 언어로 풀리며, 검색은 부분 문자열로 맞춘다. 검색엔진최적화 안의 최적화를 찾는 방법은 그것뿐이다."

[[extra.register]]
title = "인라인 스타일 대신 클래스"
body  = "구문 강조가 클래스 이름을 낸다. 인라인 색은 테마 하나를 모든 문서에 영원히 박아 넣고, 엄격한 style-src 를 불가능하게 만든다."

[[extra.register]]
title = "바이너리 하나, 런타임 없음"
body  = "Node 도 Python 도 시스템 라이브러리도 필요 없다. 내려받은 것이 곧 도는 것이다."

+++

지금 보고 있는 사이트가 이걸로 만들어졌다. [문서 사이트][docs] 도 마찬가지인데,
CI 가 방금 컴파일한 바이너리로 그 문서를 빌드하므로 문서가 생성기의 회귀 테스트
노릇을 한다.

[docs]: https://sqzass.sqzer.com
