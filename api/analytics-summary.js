// Fonction serverless Vercel : agrege les evenements de analytics_events
// pour la page interne /interne/analytics/ (templates/analytics_dashboard.html).
// Protegee par le meme jeton admin que /interne/verification-avocats/
// (header x-admin-token, variable d'environnement Vercel
// VERIFICATION_ADMIN_TOKEN -- pas besoin d'un deuxieme jeton, meme niveau
// de confiance : c'est Greg qui consulte les deux pages).
//
// GET /api/analytics-summary?days=30
//
// Aucune agregation SQL cote Supabase (pas de fonction/RPC dediee) : on
// recupere les lignes brutes de la fenetre demandee (plafonnees a
// MAX_ROWS, voir plus bas) et on agrege en JS ici, dans le meme esprit que
// admin-list.js. Simple a lire/maintenir, largement suffisant pour
// le volume de trafic de ce site ; a revisiter (vue materialisee /
// fonction Postgres) si le plafond commence a etre atteint regulierement.

const lib = require("./_verification-lib");

const MAX_ROWS = 20000;
const DEFAULT_DAYS = 30;
const MAX_DAYS = 90;
const TOP_N = 15;

function clampDays(raw) {
  const n = parseInt(raw, 10);
  if (!Number.isFinite(n) || n <= 0) return DEFAULT_DAYS;
  return Math.min(n, MAX_DAYS);
}

function topEntries(counts, n) {
  return Object.entries(counts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, n)
    .map(([key, count]) => ({ key, count }));
}

function dayKey(iso) {
  return (iso || "").slice(0, 10); // YYYY-MM-DD, assez pour regrouper par jour calendaire UTC
}

module.exports = async function handler(req, res) {
  if (req.method !== "GET") {
    res.status(405).json({ error: "method_not_allowed" });
    return;
  }
  if (!(await lib.checkAdminAuth(req))) {
    res.status(401).json({ error: "unauthorized" });
    return;
  }
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) {
    res.status(500).json({ error: "server_not_configured" });
    return;
  }

  const days = clampDays(req.query.days);
  const since = new Date(Date.now() - days * 24 * 3600 * 1000).toISOString();

  try {
    const rows = await lib.supabaseSelect(
      "analytics_events",
      `created_at=gte.${encodeURIComponent(since)}&select=event_type,path,lang,canton,referrer_domain,device_type,session_id,visitor_id,meta,created_at&order=created_at.desc&limit=${MAX_ROWS}`
    );

    const pageviews = rows.filter((r) => r.event_type === "pageview");
    const pageviewEnds = rows.filter((r) => r.event_type === "pageview_end");

    const pathCounts = {};
    const deviceCounts = {};
    const referrerCounts = {};
    const sessionPageviewCounts = {};
    const visitorDays = {}; // visitor_id -> Set of day keys seen

    for (const r of pageviews) {
      pathCounts[r.path] = (pathCounts[r.path] || 0) + 1;
      if (r.device_type) deviceCounts[r.device_type] = (deviceCounts[r.device_type] || 0) + 1;
      if (r.referrer_domain) referrerCounts[r.referrer_domain] = (referrerCounts[r.referrer_domain] || 0) + 1;
      if (r.session_id) sessionPageviewCounts[r.session_id] = (sessionPageviewCounts[r.session_id] || 0) + 1;
      if (r.visitor_id) {
        const d = dayKey(r.created_at);
        if (!visitorDays[r.visitor_id]) visitorDays[r.visitor_id] = new Set();
        if (d) visitorDays[r.visitor_id].add(d);
      }
    }

    const uniqueSessions = Object.keys(sessionPageviewCounts).length;
    const uniqueVisitors = Object.keys(visitorDays).length;
    const returningVisitors = Object.values(visitorDays).filter((set) => set.size > 1).length;
    const bouncedSessions = Object.values(sessionPageviewCounts).filter((n) => n === 1).length;

    let durationTotal = 0;
    let durationCount = 0;
    let scrollTotal = 0;
    let scrollCount = 0;
    for (const r of pageviewEnds) {
      const d = r.meta && typeof r.meta.duration_seconds === "number" ? r.meta.duration_seconds : null;
      if (d !== null && d > 0 && d < 3600) {
        durationTotal += d;
        durationCount += 1;
      }
      const s = r.meta && typeof r.meta.scroll_depth === "number" ? r.meta.scroll_depth : null;
      if (s !== null && s >= 0 && s <= 100) {
        scrollTotal += s;
        scrollCount += 1;
      }
    }

    const eventsByType = {};
    for (const r of rows) {
      eventsByType[r.event_type] = (eventsByType[r.event_type] || 0) + 1;
    }

    res.status(200).json({
      ok: true,
      range: { days, since },
      truncated: rows.length >= MAX_ROWS,
      total_events: rows.length,
      pageviews: pageviews.length,
      unique_sessions: uniqueSessions,
      unique_visitors: uniqueVisitors,
      returning_visitors: returningVisitors,
      returning_visitor_rate: uniqueVisitors ? returningVisitors / uniqueVisitors : null,
      bounce_rate: uniqueSessions ? bouncedSessions / uniqueSessions : null,
      avg_duration_seconds: durationCount ? durationTotal / durationCount : null,
      avg_scroll_depth: scrollCount ? scrollTotal / scrollCount : null,
      top_pages: topEntries(pathCounts, TOP_N),
      device_breakdown: topEntries(deviceCounts, 5),
      top_referrers: topEntries(referrerCounts, 10),
      events_by_type: topEntries(eventsByType, 20),
    });
  } catch (err) {
    res.status(502).json({ error: "summary_failed", detail: String(err.message || err) });
  }
};
