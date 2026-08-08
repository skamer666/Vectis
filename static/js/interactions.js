/* Legatis — couche d'interactivite partagee (reveal, header, compteurs, filtres) */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* -- masthead : compression + ombre au defilement -- */
  var masthead = document.querySelector('.masthead');
  if (masthead) {
    var onScrollHeader = function () {
      masthead.classList.toggle('is-scrolled', window.scrollY > 24);
    };
    onScrollHeader();
    window.addEventListener('scroll', onScrollHeader, { passive: true });
  }

  /* -- barre de progression de lecture -- */
  var progressWrap = document.createElement('div');
  progressWrap.className = 'reading-progress';
  progressWrap.innerHTML = '<div class="reading-progress-bar" id="reading-progress-bar"></div>';
  document.body.appendChild(progressWrap);
  var progressBar = document.getElementById('reading-progress-bar');
  function updateProgress() {
    var doc = document.documentElement;
    var scrollable = doc.scrollHeight - doc.clientHeight;
    var pct = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
    progressBar.style.width = Math.min(100, Math.max(0, pct)) + '%';
  }
  updateProgress();
  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress);

  /* -- retour en haut -- */
  var backToTop = document.createElement('a');
  backToTop.href = '#top';
  backToTop.className = 'back-to-top';
  backToTop.setAttribute('aria-label', 'Retour en haut de page');
  backToTop.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
  document.body.appendChild(backToTop);
  backToTop.addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
  });
  window.addEventListener('scroll', function () {
    backToTop.classList.toggle('is-visible', window.scrollY > 480);
  }, { passive: true });

  /* -- reveal au scroll : ajoute data-reveal="" a un element, stagger via data-reveal-group -- */
  var revealEls = document.querySelectorAll('[data-reveal]');
  if (revealEls.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      revealEls.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var groups = {};
      revealEls.forEach(function (el) {
        var group = el.getAttribute('data-reveal-group') || '__solo__' + Math.random();
        groups[group] = groups[group] || [];
        groups[group].push(el);
      });
      Object.keys(groups).forEach(function (g) {
        groups[g].forEach(function (el, i) {
          el.style.setProperty('--reveal-delay', Math.min(i * 0.07, 0.42) + 's');
        });
      });
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
      revealEls.forEach(function (el) { io.observe(el); });
    }
  }

  /* -- compteurs animes : anime le premier nombre trouve dans le texte, en conservant le reste -- */
  var counters = document.querySelectorAll('.stat-value');
  if (counters.length && !reduceMotion && 'IntersectionObserver' in window) {
    var counterIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        counterIo.unobserve(entry.target);
        animateCounter(entry.target);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { counterIo.observe(el); });
  }

  function animateCounter(el) {
    var raw = el.textContent;
    var match = raw.match(/[\d'’,. ]*\d/);
    if (!match) return;
    var digitsOnly = match[0].replace(/[^\d]/g, '');
    if (!digitsOnly) return;
    var target = parseInt(digitsOnly, 10);
    if (!isFinite(target) || target <= 0) return;
    var before = raw.slice(0, match.index);
    var after = raw.slice(match.index + match[0].length);
    var duration = 1100;
    var start = null;
    function easeOutExpo(t) { return t === 1 ? 1 : 1 - Math.pow(2, -10 * t); }
    function frame(ts) {
      if (start === null) start = ts;
      var elapsed = ts - start;
      var t = Math.min(1, elapsed / duration);
      var value = Math.round(easeOutExpo(t) * target);
      el.textContent = before + value.toLocaleString('fr-CH') + after;
      if (t < 1) requestAnimationFrame(frame);
      else el.textContent = raw;
    }
    requestAnimationFrame(frame);
  }

  /* -- filtre instantane generique --
     usage: <div class="filter-box"><input data-filter-input data-filter-target=".index-grid" data-filter-item=".index-cell" data-filter-field=".name"></div>
  */
  document.querySelectorAll('[data-filter-input]').forEach(function (input) {
    var itemSelector = input.getAttribute('data-filter-item');
    var fieldSelector = input.getAttribute('data-filter-field');
    var countEl = input.parentElement.querySelector('.filter-box-count');
    var scope = input.getAttribute('data-filter-scope') ? document.querySelector(input.getAttribute('data-filter-scope')) : document;
    if (!itemSelector || !scope) return;

    function normalize(s) {
      return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    }

    input.addEventListener('input', function () {
      var q = normalize(input.value.trim());
      var items = scope.querySelectorAll(itemSelector);
      var visible = 0;
      items.forEach(function (item) {
        var field = fieldSelector ? item.querySelector(fieldSelector) : item;
        var text = normalize(field ? field.textContent : item.textContent);
        var match = !q || text.indexOf(q) !== -1;
        item.classList.toggle('is-hidden', !match);
        if (match) visible++;
      });
      if (countEl) {
        countEl.textContent = q ? visible + ' resultat' + (visible !== 1 ? 's' : '') : '';
      }
    });
  });

})();
