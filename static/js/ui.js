/* 테마 토글, 스크롤 리빌, 코드 블록 복사.
 *
 * 셋 다 없어도 페이지는 읽힌다. 리빌을 숨기는 CSS 가 `.js` 뒤에 있고 그
 * 클래스는 <head> 인라인 스크립트가 붙이므로, 이 파일이 못 와도 내용이
 * 사라지지 않는다.
 */
(function () {
  "use strict";

  var root = document.documentElement;
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- theme ---------- */

  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = root.dataset.theme === "light" ? "dark" : "light";
      root.dataset.theme = next;
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* ---------- reveal ---------- */

  /* 한 번 보이면 다시 숨기지 않는다. 위로 스크롤할 때 도로 사라지는 것은
     읽던 자리로 돌아가는 사람에게 고장으로 보인다. */
  var targets = document.querySelectorAll("[data-reveal]");
  if (reduced || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("is-lit"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("is-lit");
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.05 });

    targets.forEach(function (el) {
      /* 이미 첫 화면에 들어와 있는 것은 관찰을 기다리지 않는다 — 관찰자가
         첫 콜백을 내기까지의 한 프레임이 눈에 띈다. */
      if (el.getBoundingClientRect().top < window.innerHeight * 0.9) {
        el.classList.add("is-lit");
      } else {
        io.observe(el);
      }
    });
  }

  /* ---------- copy ---------- */

  var script = document.querySelector("script[data-copy]");
  var LABEL = (script && script.dataset.copy) || "Copy";
  var DONE = (script && script.dataset.copied) || "Copied";

  if (navigator.clipboard) {
    document.querySelectorAll(".prose pre").forEach(function (pre) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "copy-btn";
      btn.textContent = LABEL;

      btn.addEventListener("click", function () {
        /* 버튼 자신의 글자가 pre 안에 있으므로 code 만 읽는다. 안 그러면
           복사한 명령 끝에 "Copy" 가 붙어 나간다. */
        var code = pre.querySelector("code") || pre;
        navigator.clipboard.writeText(code.innerText).then(function () {
          btn.textContent = DONE;
          btn.classList.add("is-done");
          setTimeout(function () {
            btn.textContent = LABEL;
            btn.classList.remove("is-done");
          }, 1600);
        });
      });

      pre.appendChild(btn);
    });
  }

  /* ---------- feature preview ---------- */

  /* 홈 맨 위 글의 미리보기. 손이 닿거나 포커스가 오면 돌고, 떠나면 첫 프레임으로
     되감는다 — 그 프레임이 곧 poster 라 되돌아간 자리가 원래 자리다.

     영상은 preload="none" 이라 여기서 play() 를 부르기 전에는 한 바이트도 받지
     않는다. 첫 화면에 700KB 를 얹지 않으려는 것이고, 그래서 이 파일이 못 와도
     남는 것은 정지 그림 한 장이다.

     동작을 줄이라는 설정이면 아무것도 걸지 않는다. 이 사이트에서 저절로 움직이는
     것은 이것 하나뿐이라, 끄라고 한 사람에게는 없는 것과 같아야 한다. */
  var feature = document.querySelector(".feature");
  var clip = feature && feature.querySelector(".feature-media");
  if (clip && !reduced) {
    var play = function () {
      var p = clip.play();
      /* 자동재생이 막히면 거절된 프로미스가 콘솔에 빨간 줄을 남긴다. 미리보기가
         안 도는 것은 고장이 아니라 브라우저의 정책이므로 조용히 삼킨다. */
      if (p && p.catch) p.catch(function () {});
    };
    var stop = function () {
      clip.pause();
      clip.currentTime = 0;
    };
    feature.addEventListener("mouseenter", play);
    feature.addEventListener("mouseleave", stop);
    /* 키보드로 온 사람도 같은 것을 본다. 미리보기가 링크 하나에 붙어 있으므로
       포커스가 곧 "지금 이걸 보고 있다"는 뜻이다. */
    feature.addEventListener("focus", play);
    feature.addEventListener("blur", stop);
  }

  /* ---------- reading rail ---------- */

  /* 넓은 화면에서 오른쪽 가장자리에 서는 목차. 항목마다 세로 헤어라인 한 칸이고,
     칸의 높이가 그 절이 글에서 차지하는 몫이다. 항목이 다 같은 크기인 목록은
     "가운데 절이 이 글의 절반"이라는 사실을 말하지 못한다.

     자료는 본문에 이미 있는 .toc 다. 이 파일이 못 오면 그 목록이 그대로 남는다 —
     목록을 감추는 CSS 가 여기서 붙이는 .has-rail 뒤에 있다.

     첫 칸은 제목에서 첫 소제목까지다. 그게 없을 때 재 보니 이 글의 34% 가 어느
     칸에도 안 들어갔고, 처음 750px 을 굴리는 동안 레일이 통째로 죽어 있었다.
     도착해서 읽기 시작한 사람에게 아무 반응이 없는 진행 표시는 고장으로 보인다.

     넓은 화면인지는 여기서 묻지 않는다. 그 판단은 main.css 의 min-width 하나가
     갖고 있다. 두 곳에 두면 두 값이 조용히 어긋나고, 그때 나오는 증상은 "레일이
     보이는데 안 찬다"라 숫자 문제로 보이지 않는다.

     이른 반환이 여러 번 필요해서 안쪽 IIFE 다. */
  (function () {
    /* 읽는 줄. 마스트헤드에 가리지 않은 높이의 위에서 30%. */
    var LINE = 0.3;
    /* 이만큼도 못 구르는 문서에는 진행 표시를 그리지 않는다. */
    var FLOOR = 240;

    var toc = document.querySelector(".toc");
    var prose = document.querySelector(".prose");
    var title = document.querySelector(".page-title");
    if (!toc || !prose) return;
    if (root.scrollHeight - window.innerHeight < FLOOR) return;

    /* 목차의 링크를 전부 쓴다. 깊이별로 고르지 않는다 — 레일이 그리는 것은
       개요가 아니라 분량이고, 분량에는 깊이가 없다. 구조는 좁은 화면의 목록이
       들여쓰기로 이미 말한다. */
    var heads = [];
    toc.querySelectorAll("a[href^='#']").forEach(function (a) {
      var href = a.getAttribute("href");
      /* 한국어 제목은 id 가 한글이다(#택하지-않은-우회로). "#"+id 를
         querySelector 에 넘기면 CSS 선택자로 파싱돼 던진다. 소스에 적힌 값을
         그대로 쓰므로 디코딩도 필요 없다. */
      var el = document.getElementById(href.slice(1));
      if (el) heads.push({ el: el, href: href, text: a.textContent });
    });
    /* 소제목이 하나뿐인 목차는 목차가 아니라 링크 하나다. */
    if (heads.length < 2) return;

    /* 첫 칸은 머리말이다. 제목을 이름으로 쓰고 <main id="content"> 로 간다 —
       건너뛰기 링크가 이미 쓰는 진짜 앵커라, 가짜 "#" 도 클릭 핸들러도 필요
       없다. */
    var parts = [{ el: prose, href: "#content", text: (title && title.textContent) || "" }]
      .concat(heads);

    var host = document.createElement("nav");
    host.className = "rail";
    /* 이름은 목록이 이미 갖고 있다. JS 안에 문자열을 두면 번역도 안 되고
       tools/fonts.py 의 눈에도 안 띈다. */
    host.setAttribute("aria-label", toc.getAttribute("aria-label") || "");

    var rows = parts.map(function (s) {
      /* 격자가 두 열이라 넣는 순서대로 이름·눈금이 한 행이 된다. 이름이 앞이고
         눈금이 뒤다 — 화면에서 이름이 안쪽, 눈금이 바깥쪽이다. */
      var label = document.createElement("a");
      label.className = "rail-label";
      label.setAttribute("href", s.href);
      label.textContent = s.text;

      var seg = document.createElement("span");
      seg.className = "rail-seg";
      var fill = document.createElement("i");
      fill.className = "rail-fill";
      seg.appendChild(fill);

      host.appendChild(label);
      host.appendChild(seg);
      return { fill: fill, label: label, el: s.el, f: -1 };
    });

    /* 목차 바로 뒤에 꽂는다. body 끝에 붙이면 화면에서는 본문 옆이지만 탭
       순서에서는 본문 뒤가 되고, 다 읽은 뒤에야 닿는 목차는 아무도 안 쓴다. */
    toc.insertAdjacentElement("afterend", host);
    root.classList.add("has-rail");

    var tops = [];
    var lead = 0;
    var at = -1;

    function absTop(el) { return el.getBoundingClientRect().top + window.scrollY; }

    /* 재는 곳은 여기 하나다. 스크롤 중에는 아무것도 재지 않고 산수만 한다. */
    function layout() {
      /* 읽는 줄이 마스트헤드에 가리는 만큼을 제목 자신의 scroll-margin-top 에서
         가져온다. main.css 가 앵커 점프를 위해 이미 선언해 둔 값이고, 브라우저가
         눌러서 뛸 때 쓰는 바로 그 값이다 — 한 군데서 나오므로 "여기 있다"와
         "여기로 간다"가 어긋날 수 없다. */
      var pad = parseFloat(getComputedStyle(heads[0].el).scrollMarginTop) || 0;
      lead = pad + (window.innerHeight - pad) * LINE;

      tops = [];
      var prev = 0;
      rows.forEach(function (r) {
        /* 앞 경계보다 위로는 못 간다. 서브픽셀이나 sticky 때문에 뒤 제목이 앞
           제목보다 위로 재어지면 높이가 음수인 칸이 생긴다. */
        prev = Math.max(absTop(r.el), prev);
        tops.push(prev);
      });
      /* 읽기는 본문이 끝나는 데서 끝난다. 페이저와 콜로폰은 글이 아니다. */
      tops.push(Math.max(absTop(prose) + prose.offsetHeight, prev + 1));

      /* 칸의 높이가 그 절의 몫이다. 아래끝을 두면 아주 짧은 절도 사라지지 않고
         두 줄짜리 이름이 옆 칸을 침범하지도 않는다.
         ponytail: 절이 열 개를 넘으면(768px 높이 화면) 아래끝의 합이 상자보다
         커져 넘치고, 그 앞에서 이미 아래끝이 몫을 눌러 두 칸의 순서를 뒤집을 수
         있다. 그때 손댈 곳은 2.2rem 과 min(64vh, 34rem) 둘이다. */
      var total = tops[tops.length - 1] - tops[0];
      var track = "";
      for (var i = 0; i < rows.length; i++) {
        track += " minmax(2.2rem, " +
                 ((tops[i + 1] - tops[i]) / total * 100).toFixed(3) + "fr)";
      }
      host.style.gridTemplateRows = track.slice(1);
      progress();
    }

    function progress() {
      if (!tops.length) return;
      var line = window.scrollY + lead;
      /* 문서 끝에 닿으면 마지막 절은 끝난 것이다. 읽는 줄은 화면 아래 한 뼘을
         영영 못 지나가므로, 이게 없으면 마지막 칸은 절대 안 찬다. */
      var done = window.scrollY + window.innerHeight >= root.scrollHeight - 2;
      /* 머리말 칸이 있으므로 첫 화면부터 현재가 있다. 도착한 사람은 실제로
         머리말을 읽고 있다. */
      var now = 0;

      for (var i = 0; i < rows.length; i++) {
        var f = done ? 1 : (line - tops[i]) / Math.max(1, tops[i + 1] - tops[i]);
        f = f < 0 ? 0 : f > 1 ? 1 : f;
        /* 값이 그대로면 손대지 않는다. 스크롤 한 번에 절 수만큼 쓰는 자리다. */
        if (rows[i].f !== f) {
          rows[i].fill.style.height = (f * 100).toFixed(2) + "%";
          rows[i].f = f;
        }
        /* 화면 상자가 아니라 줄 하나로 고른다. 제목 여럿이 같이 보일 때 누가
           이기는지 따질 일이 없다 — 줄 위에 있는 마지막 절이다. 관찰자를 쓰지
           않으므로 부드러운 스크롤과 싸울 일도 없다. */
        if (line >= tops[i]) now = i;
      }
      if (done) now = rows.length - 1;

      if (now === at) return;
      /* 눈금에는 표시를 따로 안 단다. 지금 절은 이 열에서 유일하게 덜 찬 칸이고,
         그게 이미 표시다. 이름에는 aria-current 가 붙는다 — 보조기술이 읽는 것도
         그것이고, 색은 거기서 나온다. */
      if (at >= 0) rows[at].label.removeAttribute("aria-current");
      rows[now].label.setAttribute("aria-current", "true");
      at = now;
    }

    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { ticking = false; progress(); });
    }, { passive: true });

    var timer;
    window.addEventListener("resize", function () {
      clearTimeout(timer);
      timer = setTimeout(layout, 120);
    });

    /* 한글 서브셋은 unicode-range 뒤에 있어서 첫 페인트 뒤에 온다. 오면 본문
       높이가 바뀌고, 그 전에 잰 경계는 전부 틀린 값이 된다. */
    window.addEventListener("load", layout);
    if ("ResizeObserver" in window) new ResizeObserver(layout).observe(prose);

    layout();
  })();
})();
