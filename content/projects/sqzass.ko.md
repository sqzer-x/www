+++
title = "sqzass"
description = "Rust 로 만든 정적 사이트 생성기. 이 사이트가 그걸로 만들어졌다."
weight = 10
date = 2026-07-31

[extra]
tier = "landing"

eyebrow  = "정적 사이트 생성기 · Rust"
tagline  = "대부분의 생성기는 예쁜 URL 과 리다이렉트, 캐시 헤더를 호스트에 맡긴다. sqzass 는 그 일을 직접 한다. 그래서 같은 출력이 GitHub Pages 에서도, Vercel 에서도, 평범한 HTTP 로 디렉터리를 내주는 서버에서도 똑같이 맞다."
lang     = "Rust"
license  = "MIT"
version  = "0.1.0"
platform = "Linux · macOS"
repo     = "https://github.com/sqzer-x/sqzass"
stars     = 0
accent     = "#e0a06a"
mark     = "images/projects/sqzass.png"
logo     = ""

actions = [
  { label = "문서", url = "https://sqzass.sqzer.com",          style = "primary" },
  { label = "소스", url = "https://github.com/sqzer-x/sqzass", style = "ghost"   },
]

facts = [
  { value = "25 ms",  label = "1,000 페이지" },
  { value = "0",      label = "런타임 의존성" },
  { value = "0.1.0",  label = "버전" },
  { value = "MIT",    label = "라이선스" },
]

features_eyebrow = "설계"
features_title   = "여섯 개의 결정과 각각의 근거"
features_intro   = "취향이 아니다. 하나하나가 다른 데서 먼저 일어난 사고다."
# 항목은 아래 [[extra.features]] 에 있다. 인라인 테이블은 TOML 1.0 에서
# 한 줄을 넘지 못하고, 이 설명들은 한 줄에 들어가지 않는다.

session_eyebrow = "빠른 시작"
session_title   = "파일 세 개, 그다음이 사이트"
session_shell   = "zsh"
session_caption = "실제 출력이다. 이 레포의 문서 사이트가 60 페이지다."
session_lines = [
  { kind = "cmd",     text = "$ sqzass init mysite" },
  { kind = "comment", text = "# sqzass.toml, content/_index.md, templates/page.html 을 쓴다" },
  { kind = "cmd",     text = "$ sqzass serve -i mysite" },
  { kind = "out",     text = "  http://127.0.0.1:3000   라이브 리로드" },
  { kind = "cmd",     text = "$ sqzass build -i docs" },
  { kind = "out",     text = "  60 pages → docs/public" },
]

cta_title = "문서를 읽어 보세요."
cta_text  = "같은 레포의 docs 디렉터리에서 sqzass 로 만들어진다. CI 가 방금 컴파일한 바이너리로 그 문서를 빌드한다."
cta_actions = [
  { label = "sqzass.sqzer.com", url = "https://sqzass.sqzer.com",          style = "primary" },
  { label = "소스",             url = "https://github.com/sqzer-x/sqzass", style = "ghost"   },
]

[[extra.features]]
title = "깨진 참조는 빌드를 세운다"
desc  = "풀리지 않는 링크, 없는 템플릿, 같은 URL 을 주장하는 두 페이지, 오타 난 설정 키. 전부 경고가 아니라 에러다."

[[extra.features]]
title = "마크다운은 AST 에서 다룬다"
desc  = "링크 재작성, 제목 앵커, 목차가 전부 트리 연산이다. 완성된 HTML 에 정규식을 돌리면 작은따옴표로 감싼 속성을 조용히 건너뛴다."

[[extra.features]]
title = "바이트까지 같은 빌드"
desc  = "같은 입력을 두 번 빌드하면 같은 바이트가 나오고, CI 가 푸시마다 확인한다. 렌더는 병렬이고, 결정성은 일정이 아니라 병합이 만든다."

[[extra.features]]
title = "한국어는 나중에 얹은 것이 아니다"
desc  = "번역이 원문 옆에 있고, 링크는 읽는 사람의 언어로 풀리며, 검색은 부분 문자열로 맞춘다. 검색엔진최적화 안의 최적화를 찾는 방법은 그것뿐이다."

[[extra.features]]
title = "인라인 스타일 대신 클래스"
desc  = "구문 강조가 클래스 이름을 낸다. 인라인 색은 테마 하나를 모든 문서에 영원히 박아 넣고, 엄격한 style-src 를 불가능하게 만든다."

[[extra.features]]
title = "바이너리 하나, 런타임 없음"
desc  = "Node 도 Python 도 시스템 라이브러리도 필요 없다. 내려받은 것이 곧 도는 것이다."

+++

지금 보고 있는 사이트가 이걸로 만들어졌다. [문서 사이트][docs] 도 마찬가지인데,
CI 가 방금 컴파일한 바이너리로 그 문서를 빌드하므로 문서가 생성기의 회귀 테스트
노릇을 한다.

[docs]: https://sqzass.sqzer.com
