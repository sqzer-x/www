/* 검색 팔레트. 의존성 없음.
 *
 * sqzass 가 언어마다 색인을 하나씩 낸다. 각 행은 페이지 하나이고
 * `t` 제목, `d` 설명, `u` URL, `s` 갈래 이름, `c` 본문 텍스트다. `d` 와 `s` 는
 * 비어 있으면 아예 없다 — 그래서 읽을 때마다 있는지 확인한다.
 *
 * 단어가 아니라 부분 문자열로 찾는다. 한국어는 명사에 조사가 붙고 띄어쓰기
 * 없이 합성어를 만들기 때문에, 단어 색인으로는 `검색엔진최적화` 안의 `최적화` 를
 * 영영 찾지 못한다.
 *
 * 다이얼로그는 <dialog> 다. Escape, 백드롭, 포커스 트랩, 닫을 때 트리거로
 * 포커스 되돌리기가 전부 플랫폼 동작이라 우리가 쓸 코드가 아니다.
 */
(function () {
  "use strict";

  var trigger = document.querySelector(".search-trigger");
  var dialog = document.getElementById("search-dialog");
  if (!trigger || !dialog || !dialog.showModal) return;

  var input = dialog.querySelector(".palette-input");
  var list = dialog.querySelector(".palette-results");
  var status = dialog.querySelector(".palette-status");
  var script = document.querySelector("script[data-empty]");
  var EMPTY = (script && script.dataset.empty) || "No matches.";
  var HINT = (script && script.dataset.hint) || "";

  var rows = null;
  var loading = false;
  var cursor = -1;

  /* 수정자 키를 읽는 사람의 것으로 바꿔 쓴다. 템플릿이 쓴 값은 JS 가 없을 때의 것. */
  var mac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);
  var kbd = trigger.querySelector("kbd");
  if (kbd) kbd.textContent = mac ? "⌘ K" : "Ctrl K";

  function load() {
    if (rows || loading) return Promise.resolve();
    loading = true;
    status.textContent = "…";
    return fetch(trigger.dataset.index)
      .then(function (r) { return r.json(); })
      .then(function (data) { rows = data; status.textContent = HINT; })
      .catch(function () { status.textContent = EMPTY; })
      .then(function () { loading = false; });
  }

  function open() {
    load().then(function () { render(input.value); });
    if (!dialog.open) dialog.showModal();
    input.focus();
    input.select();
  }

  /* 제목에 걸린 것이 설명보다, 설명이 본문보다 위다. 제목이 그 말로 시작하면
     한 번 더 올라간다 — 찾던 것을 정확히 친 경우다. */
  function score(row, terms) {
    var t = row.t.toLowerCase();
    var d = (row.d || "").toLowerCase();
    var c = row.c.toLowerCase();
    var total = 0;
    for (var i = 0; i < terms.length; i++) {
      var q = terms[i];
      if (t.indexOf(q) === 0) total += 100;
      else if (t.indexOf(q) > -1) total += 60;
      else if (d.indexOf(q) > -1) total += 25;
      else if (c.indexOf(q) > -1) total += 8;
      else return -1; /* 모든 낱말이 어딘가에는 있어야 한다. OR 이 아니라 AND. */
    }
    return total;
  }

  function mark(text, terms) {
    var frag = document.createDocumentFragment();
    var lower = text.toLowerCase();
    var at = -1, len = 0;
    for (var i = 0; i < terms.length; i++) {
      var p = lower.indexOf(terms[i]);
      if (p > -1 && (at === -1 || p < at)) { at = p; len = terms[i].length; }
    }
    if (at === -1) { frag.appendChild(document.createTextNode(text)); return frag; }
    frag.appendChild(document.createTextNode(text.slice(0, at)));
    var m = document.createElement("mark");
    m.textContent = text.slice(at, at + len);
    frag.appendChild(m);
    frag.appendChild(document.createTextNode(text.slice(at + len)));
    return frag;
  }

  function render(query) {
    list.textContent = "";
    cursor = -1;
    var q = query.trim().toLowerCase();
    if (!rows || !q) { status.textContent = rows ? HINT : status.textContent; return; }

    var terms = q.split(/\s+/);
    var hits = [];
    for (var i = 0; i < rows.length; i++) {
      var s = score(rows[i], terms);
      if (s > -1) hits.push({ row: rows[i], score: s });
    }
    /* 같은 점수면 제목순. 순서가 매번 달라지면 두 번째 검색에서 눈이 길을 잃는다. */
    hits.sort(function (a, b) { return b.score - a.score || a.row.t.localeCompare(b.row.t); });
    hits = hits.slice(0, 12);

    if (!hits.length) { status.textContent = EMPTY; return; }
    status.textContent = String(hits.length);

    hits.forEach(function (h) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = h.row.u;

      var title = document.createElement("span");
      title.className = "palette-title";
      title.appendChild(mark(h.row.t, terms));
      a.appendChild(title);

      var sub = h.row.s || h.row.d;
      if (sub) {
        var crumb = document.createElement("span");
        crumb.className = "palette-crumb";
        crumb.textContent = sub;
        a.appendChild(crumb);
      }

      li.appendChild(a);
      list.appendChild(li);
    });
  }

  function move(step) {
    var items = list.children;
    if (!items.length) return;
    if (cursor > -1) items[cursor].removeAttribute("aria-selected");
    cursor = (cursor + step + items.length) % items.length;
    items[cursor].setAttribute("aria-selected", "true");
    items[cursor].scrollIntoView({ block: "nearest" });
  }

  trigger.addEventListener("click", open);

  document.addEventListener("keydown", function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      open();
    }
  });

  input.addEventListener("input", function () { render(input.value); });

  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
    else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
    else if (e.key === "Enter") {
      /* 폼 안이라 Enter 는 기본적으로 다이얼로그를 닫는다. 고른 것이 있으면
         닫는 대신 거기로 간다. */
      var pick = cursor > -1 ? list.children[cursor] : list.children[0];
      if (pick) { e.preventDefault(); pick.querySelector("a").click(); }
    }
  });

  /* 닫힐 때 비워 둔다. 다시 열었을 때 지난 검색 결과가 남아 있으면, 방금
     친 것에 대한 답으로 읽힌다. */
  dialog.addEventListener("close", function () {
    input.value = "";
    list.textContent = "";
    status.textContent = "";
    cursor = -1;
  });

  /* 백드롭 클릭. <dialog> 는 백드롭도 자기 자신을 target 으로 준다. */
  dialog.addEventListener("click", function (e) {
    if (e.target === dialog) dialog.close();
  });
})();
