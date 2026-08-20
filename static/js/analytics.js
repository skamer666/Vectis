/* Analytics "maison", respectueuse de la vie privee -- voir la section
 * analytics_events de supabase_schema.sql pour le detail des choix
 * (aucune IP stockee, aucun cookie, aucune URL de referrer complete,
 * aucune empreinte navigateur detaillee). Envoie les evenements a
 * /api/track (api/track.js), qui les insere dans Supabase.
 *
 * Deux identifiants generes cote client, jamais lies a une identite :
 *   - session_id (sessionStorage) : remis a zero a chaque nouvelle session
 *     de navigation, sert a compter les pages par session / le taux de
 *     rebond.
 *   - visitor_id (localStorage) : UUID aleatoire persistant mais anonyme,
 *     sert uniquement a des compteurs agreges (ex: % de visiteurs revenus
 *     un autre jour) -- jamais expose individuellement dans le tableau de
 *     bord interne.
 *
 * Respecte "Do Not Track" : si le navigateur l'indique, les identifiants
 * sont quand meme generes (pour ne rien casser cote page) mais aucun
 * evenement n'est jamais envoye.
 */
(function () {
  "use strict";

  var TRACK_URL = "/api/track";

  function dntEnabled() {
    var v = navigator.doNotTrack || window.doNotTrack || navigator.msDoNotTrack;
    return v === "1" || v === "yes";
  }

  function uuid() {
    if (window.crypto && typeof window.crypto.randomUUID === "function") {
      return window.crypto.randomUUID();
    }
    // Repli simple (pas besoin de qualite cryptographique ici : c'est un
    // identifiant anonyme, pas un secret).
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
      var r = (Math.random() * 16) | 0;
      var v = c === "x" ? r : (r & 0x3) | 0x8;
      return v.toString(16);
    });
  }

  function getOrCreate(storage, key) {
    try {
      var existing = storage.getItem(key);
      if (existing) return existing;
      var fresh = uuid();
      storage.setItem(key, fresh);
      return fresh;
    } catch (e) {
      // Navigation privee / stockage bloque : identifiant ephemere en memoire.
      return uuid();
    }
  }

  var sessionId = getOrCreate(window.sessionStorage, "legatis:sid");
  var visitorId = getOrCreate(window.localStorage, "legatis:vid");

  function deviceType() {
    var w = window.innerWidth || document.documentElement.clientWidth;
    if (w < 760) return "mobile";
    if (w < 1024) return "tablet";
    return "desktop";
  }

  function referrerDomain() {
    if (!document.referrer) return null;
    try {
      var host = new URL(document.referrer).hostname;
      if (!host || host === window.location.hostname) return null; // navigation interne, pas interessant
      return host.slice(0, 200);
    } catch (e) {
      return null;
    }
  }

  function send(eventType, meta) {
    if (dntEnabled()) return;
    var payload = {
      event_type: eventType,
      path: window.location.pathname,
      lang: document.documentElement.lang || null,
      referrer_domain: referrerDomain(),
      device_type: deviceType(),
      session_id: sessionId,
      visitor_id: visitorId,
      meta: meta || undefined,
    };
    var body = JSON.stringify(payload);
    try {
      if (navigator.sendBeacon) {
        var blob = new Blob([body], { type: "application/json" });
        var ok = navigator.sendBeacon(TRACK_URL, blob);
        if (ok) return;
      }
    } catch (e) {
      /* repli sur fetch ci-dessous */
    }
    try {
      fetch(TRACK_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: body, keepalive: true }).catch(function () {});
    } catch (e) {
      /* on n'interrompt jamais la navigation pour une erreur d'analytics */
    }
  }

  // Expose une fonction globale pour que d'autres scripts de la page
  // (formulaire de contact, boutons favori/comparer, widgets calculateurs...)
  // puissent envoyer leurs propres evenements, ex :
  //   window.legatisTrack('lead_submit', { page_type: 'avocat' });
  window.legatisTrack = send;

  send("pageview");

  var maxScrollDepth = 0;
  function updateScrollDepth() {
    var doc = document.documentElement;
    var scrollable = doc.scrollHeight - doc.clientHeight;
    var pct = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 100;
    if (pct > maxScrollDepth) maxScrollDepth = Math.min(100, Math.round(pct));
  }
  window.addEventListener("scroll", updateScrollDepth, { passive: true });

  var startedAt = Date.now();
  var endSent = false;
  function sendPageviewEnd() {
    if (endSent) return;
    endSent = true;
    updateScrollDepth();
    var durationSeconds = Math.round((Date.now() - startedAt) / 1000);
    send("pageview_end", { duration_seconds: durationSeconds, scroll_depth: maxScrollDepth });
  }
  window.addEventListener("pagehide", sendPageviewEnd);
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden") sendPageviewEnd();
  });
})();
