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
})();
