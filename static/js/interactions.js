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

  /* -- selecteur guide (page d'accueil) -- */
  var wizardForm = document.getElementById('wizard-form');
  if (wizardForm) {
    wizardForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var canton = document.getElementById('wizard-canton').value;
      var domaine = document.getElementById('wizard-domaine').value;
      var matrix = window.__legatisCrossMatrix || {};
      if (canton && domaine && matrix[canton] && matrix[canton][domaine]) {
        window.location.href = matrix[canton][domaine];
      }
    });
  }

  /* ======================================================================
     Favoris + Comparateur — stockage local, boutons injectes, barres
     flottantes, panneau lateral / modal de comparaison
     ====================================================================== */
  var I18N = window.__legatisI18N || {};
  var STORAGE_FAV = 'legatis:favorites';
  var STORAGE_CMP = 'legatis:compare';
  var CMP_MAX = 3;

  var ICON_HEART = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.6s-7.2-4.4-9.6-8.8C.8 8.4 2.2 5 5.6 5c2 0 3.4 1.2 4.6 2.7C11.4 6.2 12.8 5 14.8 5c3.4 0 4.8 3.4 3.2 6.8-2.4 4.4-9.6 8.8-9.6 8.8z"/></svg>';
  var ICON_HEART_FILLED = '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 20.6s-7.2-4.4-9.6-8.8C.8 8.4 2.2 5 5.6 5c2 0 3.4 1.2 4.6 2.7C11.4 6.2 12.8 5 14.8 5c3.4 0 4.8 3.4 3.2 6.8-2.4 4.4-9.6 8.8-9.6 8.8z"/></svg>';
  var ICON_SCALE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3v18M4 7l5-2 5 2M16 9l-3 6h6l-3-6zM4 15l-3 6h6l-3-6z" transform="translate(1,0)"/></svg>';
  var ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L19 7"/></svg>';
  var ICON_CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 6l12 12M18 6L6 18"/></svg>';
  var ICON_TRASH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M9 7V5a1 1 0 011-1h4a1 1 0 011 1v2m-8 0l1 12a1 1 0 001 1h6a1 1 0 001-1l1-12"/></svg>';

  function t(key, fallback) { return I18N[key] || fallback || key; }

  function readStore(key) {
    try { return JSON.parse(localStorage.getItem(key) || '[]'); } catch (e) { return []; }
  }
  function writeStore(key, arr) {
    try { localStorage.setItem(key, JSON.stringify(arr)); } catch (e) {}
  }
  function findIndexByUrl(list, url) {
    for (var i = 0; i < list.length; i++) { if (list[i].url === url) return i; }
    return -1;
  }

  function toggleFavorite(entry) {
    var list = readStore(STORAGE_FAV);
    var idx = findIndexByUrl(list, entry.url);
    var nowActive;
    if (idx === -1) { list.push(entry); nowActive = true; }
    else { list.splice(idx, 1); nowActive = false; }
    writeStore(STORAGE_FAV, list);
    refreshFavBar();
    return nowActive;
  }

  function toggleCompare(entry) {
    var list = readStore(STORAGE_CMP);
    var idx = findIndexByUrl(list, entry.url);
    if (idx !== -1) { list.splice(idx, 1); writeStore(STORAGE_CMP, list); refreshCompareBar(); return { active: false }; }
    if (list.length >= CMP_MAX) { return { active: false, blocked: true }; }
    list.push(entry);
    writeStore(STORAGE_CMP, list);
    refreshCompareBar();
    return { active: true };
  }

  function buildEntryFromRow(row) {
    var nameEl = row.querySelector('.registry-name');
    var firmEl = row.querySelector('.registry-firm');
    var cityEl = row.querySelector('.registry-city');
    return {
      url: row.getAttribute('href') || window.location.href,
      nom: nameEl ? nameEl.textContent.trim() : '',
      etude: firmEl ? firmEl.textContent.trim() : '',
      ville: cityEl ? cityEl.textContent.trim() : ''
    };
  }

  function enhanceRegistryRow(row) {
    if (!row || row.dataset.legatisEnhanced) return;
    var entry = buildEntryFromRow(row);
    if (!entry.nom || !entry.url) return;
    row.dataset.legatisEnhanced = '1';
    row.classList.add('has-fav-btn');

    var favBtn = document.createElement('button');
    favBtn.type = 'button';
    favBtn.className = 'fav-btn';
    favBtn.setAttribute('aria-label', t('favorite_add', 'Favoris'));
    favBtn.innerHTML = ICON_HEART;
    if (findIndexByUrl(readStore(STORAGE_FAV), entry.url) !== -1) {
      favBtn.classList.add('is-active');
      favBtn.innerHTML = ICON_HEART_FILLED;
    }
    favBtn.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      var active = toggleFavorite(entry);
      favBtn.classList.toggle('is-active', active);
      favBtn.innerHTML = active ? ICON_HEART_FILLED : ICON_HEART;
    });

    var cmpBtn = document.createElement('button');
    cmpBtn.type = 'button';
    cmpBtn.className = 'compare-btn';
    cmpBtn.setAttribute('aria-label', t('compare_add', 'Comparer'));
    cmpBtn.innerHTML = ICON_SCALE;
    if (findIndexByUrl(readStore(STORAGE_CMP), entry.url) !== -1) {
      cmpBtn.classList.add('is-active'); cmpBtn.innerHTML = ICON_CHECK;
    }
    cmpBtn.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      var res = toggleCompare(entry);
      if (res.blocked) { return; }
      cmpBtn.classList.toggle('is-active', res.active);
      cmpBtn.innerHTML = res.active ? ICON_CHECK : ICON_SCALE;
    });

    row.appendChild(favBtn);
    row.appendChild(cmpBtn);
  }
  window.legatisEnhanceRow = enhanceRegistryRow;

  document.querySelectorAll('.registry-row').forEach(enhanceRegistryRow);

  /* -- boutons profil (fiche avocat / etude) -- */
  document.querySelectorAll('.profile-fav-btn').forEach(function (btn) {
    var entry;
    try { entry = JSON.parse(btn.getAttribute('data-entry') || '{}'); } catch (e) { entry = {}; }
    if (!entry.url) entry.url = window.__legatisCanonical || window.location.href;
    if (findIndexByUrl(readStore(STORAGE_FAV), entry.url) !== -1) btn.classList.add('is-active');
    updateProfileFavLabel(btn);
    btn.addEventListener('click', function () {
      var active = toggleFavorite(entry);
      btn.classList.toggle('is-active', active);
      updateProfileFavLabel(btn);
    });
  });
  function updateProfileFavLabel(btn) {
    var span = btn.querySelector('.profile-fav-btn-label');
    if (!span) return;
    span.textContent = btn.classList.contains('is-active') ? t('favorite_remove', 'Retirer des favoris') : t('favorite_add', 'Ajouter aux favoris');
  }

  document.querySelectorAll('.profile-compare-btn').forEach(function (btn) {
    var entry;
    try { entry = JSON.parse(btn.getAttribute('data-entry') || '{}'); } catch (e) { entry = {}; }
    if (!entry.url) entry.url = window.__legatisCanonical || window.location.href;
    if (findIndexByUrl(readStore(STORAGE_CMP), entry.url) !== -1) btn.classList.add('is-active');
    updateProfileCmpLabel(btn);
    btn.addEventListener('click', function () {
      var res = toggleCompare(entry);
      if (res.blocked) return;
      btn.classList.toggle('is-active', res.active);
      updateProfileCmpLabel(btn);
    });
  });
  function updateProfileCmpLabel(btn) {
    var span = btn.querySelector('.profile-fav-btn-label');
    if (!span) return;
    span.textContent = btn.classList.contains('is-active') ? t('compare_remove', 'Retirer du comparatif') : t('compare_add', 'Comparer');
  }

  /* -- barres flottantes -- */
  var floatStack = document.createElement('div');
  floatStack.className = 'float-bar-stack';
  document.body.appendChild(floatStack);

  var favBar = document.createElement('div');
  favBar.className = 'float-bar';
  favBar.innerHTML =
    '<span class="float-bar-label">' + t('favorites_bar_label', 'Favoris') + '</span>' +
    '<span class="float-bar-count" id="fav-bar-count">0</span>' +
    '<button type="button" class="float-bar-action" id="fav-bar-open">' + t('favorites_title', 'Mes favoris') + '</button>' +
    '<button type="button" class="float-bar-close" id="fav-bar-close" aria-label="' + t('close', 'Fermer') + '">' + ICON_CLOSE + '</button>';
  floatStack.appendChild(favBar);

  var cmpBar = document.createElement('div');
  cmpBar.className = 'float-bar';
  cmpBar.innerHTML =
    '<span class="float-bar-label">' + t('compare_bar_label', 'Comparer') + '</span>' +
    '<span class="float-bar-count" id="cmp-bar-count">0</span>' +
    '<button type="button" class="float-bar-action" id="cmp-bar-open">' + t('compare_view', 'Voir la comparaison') + '</button>' +
    '<button type="button" class="float-bar-close" id="cmp-bar-close" aria-label="' + t('close', 'Fermer') + '">' + ICON_CLOSE + '</button>';
  floatStack.appendChild(cmpBar);

  function refreshFavBar() {
    var list = readStore(STORAGE_FAV);
    document.getElementById('fav-bar-count').textContent = list.length;
    favBar.classList.toggle('is-visible', list.length > 0);
    if (favPanelBody) renderFavPanel();
  }
  function refreshCompareBar() {
    var list = readStore(STORAGE_CMP);
    document.getElementById('cmp-bar-count').textContent = list.length;
    cmpBar.classList.toggle('is-visible', list.length > 0);
    if (cmpModalBody) renderCompareModal();
  }
  document.getElementById('fav-bar-close').addEventListener('click', function () {
    favBar.classList.remove('is-visible');
  });
  document.getElementById('cmp-bar-close').addEventListener('click', function () {
    cmpBar.classList.remove('is-visible');
  });

  /* -- panneau favoris -- */
  var favOverlay = document.createElement('div');
  favOverlay.className = 'panel-overlay';
  favOverlay.innerHTML =
    '<aside class="side-panel">' +
    '  <div class="side-panel-head"><h2>' + t('favorites_title', 'Mes favoris') + '</h2>' +
    '    <button type="button" class="side-panel-close" id="fav-panel-close" aria-label="' + t('close', 'Fermer') + '">' + ICON_CLOSE + '</button>' +
    '  </div>' +
    '  <div class="side-panel-body" id="fav-panel-body"></div>' +
    '</aside>';
  document.body.appendChild(favOverlay);
  var favPanelBody = null;

  document.getElementById('fav-bar-open').addEventListener('click', function () {
    favPanelBody = document.getElementById('fav-panel-body');
    renderFavPanel();
    favOverlay.classList.add('is-open');
  });
  document.getElementById('fav-panel-close').addEventListener('click', closeFavPanel);
  favOverlay.addEventListener('click', function (e) { if (e.target === favOverlay) closeFavPanel(); });
  function closeFavPanel() { favOverlay.classList.remove('is-open'); }

  function renderFavPanel() {
    var list = readStore(STORAGE_FAV);
    var body = document.getElementById('fav-panel-body');
    if (!body) return;
    if (!list.length) {
      body.innerHTML = '<p class="side-panel-empty">' + t('favorites_empty', 'Aucun favori pour l’instant.') + '</p>';
      return;
    }
    body.innerHTML = '';
    list.forEach(function (entry) {
      var row = document.createElement('div');
      row.className = 'side-panel-item';
      var meta = [entry.etude, entry.ville].filter(Boolean).join(' · ');
      row.innerHTML =
        '<div><a class="side-panel-item-name" href="' + entry.url + '">' + escapeHtmlGlobal(entry.nom) + '</a>' +
        (meta ? '<div class="side-panel-item-meta">' + escapeHtmlGlobal(meta) + '</div>' : '') + '</div>' +
        '<button type="button" class="side-panel-item-remove" aria-label="' + t('favorite_remove', 'Retirer') + '">' + ICON_TRASH + '</button>';
      row.querySelector('.side-panel-item-remove').addEventListener('click', function () {
        toggleFavorite(entry);
        document.querySelectorAll('.fav-btn.is-active').forEach(function (b) {});
        syncRowButtonsState();
      });
      body.appendChild(row);
    });
  }

  /* -- modal comparateur -- */
  var cmpModal = document.createElement('div');
  cmpModal.className = 'compare-modal';
  cmpModal.innerHTML =
    '<div class="compare-modal-inner">' +
    '  <div class="compare-modal-head"><h2>' + t('compare_title', 'Comparatif') + '</h2>' +
    '    <div style="display:flex; gap:8px; align-items:center;">' +
    '      <button type="button" class="cta-btn" id="cmp-clear">' + t('compare_clear', 'Vider') + '</button>' +
    '      <button type="button" class="side-panel-close" id="cmp-modal-close" aria-label="' + t('close', 'Fermer') + '">' + ICON_CLOSE + '</button>' +
    '    </div>' +
    '  </div>' +
    '  <div class="compare-modal-body" id="cmp-modal-body"></div>' +
    '</div>';
  document.body.appendChild(cmpModal);
  var cmpModalBody = null;

  document.getElementById('cmp-bar-open').addEventListener('click', function () {
    cmpModalBody = document.getElementById('cmp-modal-body');
    renderCompareModal();
    cmpModal.classList.add('is-open');
  });
  document.getElementById('cmp-modal-close').addEventListener('click', closeCompareModal);
  cmpModal.addEventListener('click', function (e) { if (e.target === cmpModal) closeCompareModal(); });
  function closeCompareModal() { cmpModal.classList.remove('is-open'); }
  document.getElementById('cmp-clear').addEventListener('click', function () {
    writeStore(STORAGE_CMP, []);
    refreshCompareBar();
    syncRowButtonsState();
  });

  function escapeHtmlGlobal(s) {
    var d = document.createElement('div');
    d.textContent = s || '';
    return d.innerHTML;
  }

  function renderCompareModal() {
    var list = readStore(STORAGE_CMP);
    var body = document.getElementById('cmp-modal-body');
    if (!body) return;
    if (!list.length) {
      body.innerHTML = '<p class="side-panel-empty">' + t('compare_empty', 'Ajoutez jusqu’à 3 avocats pour les comparer.') + '</p>';
      return;
    }
    var fieldDefs = [
      { key: 'etude', label: t('firm', 'Étude') },
      { key: 'ville', label: t('address', 'Ville') },
      { key: 'canton_name', label: t('canton', 'Canton') },
      { key: 'role_or_titre', label: t('practice_areas', 'Titre') },
      { key: 'langues', label: t('languages_spoken', 'Langues') },
      { key: 'seniority_text', label: '' }
    ];
    var usedFields = fieldDefs.filter(function (f) {
      return list.some(function (e) { return e[f.key]; });
    });
    var html = '<table class="compare-table"><thead><tr><th></th>';
    list.forEach(function (entry) {
      html += '<th class="compare-col-head"><a href="' + entry.url + '" style="color:inherit; text-decoration:none;">' + escapeHtmlGlobal(entry.nom) + '</a></th>';
    });
    html += '</tr></thead><tbody>';
    usedFields.forEach(function (f) {
      if (!f.label) return;
      html += '<tr><td>' + escapeHtmlGlobal(f.label) + '</td>';
      list.forEach(function (entry) {
        html += '<td>' + escapeHtmlGlobal(entry[f.key] || '—') + '</td>';
      });
      html += '</tr>';
    });
    html += '<tr><td></td>';
    list.forEach(function (entry) {
      html += '<td class="compare-remove-cell"><button type="button" class="cta-btn" data-remove-url="' + escapeHtmlGlobal(entry.url) + '">' + ICON_TRASH + '</button></td>';
    });
    html += '</tr></tbody></table>';
    body.innerHTML = html;
    body.querySelectorAll('[data-remove-url]').forEach(function (b) {
      b.addEventListener('click', function () {
        var list2 = readStore(STORAGE_CMP);
        var idx = findIndexByUrl(list2, b.getAttribute('data-remove-url'));
        if (idx !== -1) { list2.splice(idx, 1); writeStore(STORAGE_CMP, list2); refreshCompareBar(); syncRowButtonsState(); }
      });
    });
  }

  function syncRowButtonsState() {
    var favList = readStore(STORAGE_FAV);
    var cmpList = readStore(STORAGE_CMP);
    document.querySelectorAll('.registry-row[data-legatis-enhanced]').forEach(function (row) {
      var url = row.getAttribute('href');
      var fb = row.querySelector('.fav-btn');
      var cb = row.querySelector('.compare-btn');
      if (fb) {
        var isFav = findIndexByUrl(favList, url) !== -1;
        fb.classList.toggle('is-active', isFav);
        fb.innerHTML = isFav ? ICON_HEART_FILLED : ICON_HEART;
      }
      if (cb) {
        var isCmp = findIndexByUrl(cmpList, url) !== -1;
        cb.classList.toggle('is-active', isCmp);
        cb.innerHTML = isCmp ? ICON_CHECK : ICON_SCALE;
      }
    });
    document.querySelectorAll('.profile-fav-btn').forEach(function (btn) {
      var entry; try { entry = JSON.parse(btn.getAttribute('data-entry') || '{}'); } catch (e) { entry = {}; }
      var active = findIndexByUrl(favList, entry.url || window.__legatisCanonical) !== -1;
      btn.classList.toggle('is-active', active);
      updateProfileFavLabel(btn);
    });
    document.querySelectorAll('.profile-compare-btn').forEach(function (btn) {
      var entry; try { entry = JSON.parse(btn.getAttribute('data-entry') || '{}'); } catch (e) { entry = {}; }
      var active = findIndexByUrl(cmpList, entry.url || window.__legatisCanonical) !== -1;
      btn.classList.toggle('is-active', active);
      updateProfileCmpLabel(btn);
    });
  }

  refreshFavBar();
  refreshCompareBar();

  /* ======================================================================
     Capture email discrete (lead magnet) — envoie vers /api/lead-capture
     ====================================================================== */
  document.querySelectorAll('.lead-capture-form').forEach(function (form) {
    var msgEl = form.parentElement.querySelector('.lead-capture-msg');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var emailInput = form.querySelector('input[type="email"]');
      var hp = form.querySelector('.lead-capture-hp');
      if (hp && hp.value) { return; } // honeypot
      var email = emailInput.value.trim();
      if (!email || email.indexOf('@') === -1) return;
      var btn = form.querySelector('button');
      btn.disabled = true;
      fetch('/api/lead-capture', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: email,
          page_url: window.__legatisCanonical || window.location.href,
          page_title: document.title,
          lang: window.__legatisLang || 'fr',
          website: hp ? hp.value : ''
        })
      }).then(function (r) {
        if (!r.ok) throw new Error('bad_response');
        return r.json();
      }).then(function () {
        if (msgEl) { msgEl.textContent = t('lead_capture_success', 'Merci !'); msgEl.className = 'lead-capture-msg is-success'; }
        form.reset();
      }).catch(function () {
        if (msgEl) { msgEl.textContent = t('lead_capture_error', 'Erreur, réessayez.'); msgEl.className = 'lead-capture-msg is-error'; }
      }).finally(function () {
        btn.disabled = false;
      });
    });
  });

})();
