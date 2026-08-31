// Fonction Cloudflare Pages : remet a zero le compte de test avocat
// (build.py:TEST_LAWYER_SLUG, "Compte Test Legatis", canton GE) comme si
// personne ne s'etait jamais connecte -- pour pouvoir rejouer le parcours
// "verifier mon identite -> creer un compte -> se connecter -> mon profil"
// depuis /interne/verification-avocats/ sans devoir aller nettoyer Supabase
// a la main a chaque fois.
//
// POST (pas de body), header Authorization: Bearer <jwt admin> -- meme
// protection que les autres points d'acces internes (voir checkAdminAuth
// dans _verification-lib.js).
//
// Supprime, pour ce canton+cette fiche uniquement (jamais un slug arbitraire
// choisi par l'appelant, la cible est fixe en dur ci-dessous) :
//   - toutes les demandes de verification (verification_requests), quel que
//     soit leur statut (pending/approved/rejected), et les documents/selfies
//     restants dans le bucket prive verification-documents ;
//   - le compte Supabase Auth (auth.users) correspondant, qu'il ait ete cree
//     via une demande en attente (pending_user_id) ou deja active
//     (lawyer_accounts.user_id) -- la suppression cascade automatiquement
//     lawyer_accounts et lawyer_profile_submissions (on delete cascade, voir
//     supabase_schema.sql), donc pas besoin de les supprimer separement ;
//   - les photos de profil eventuellement soumises, dans le bucket public
//     lawyer-photos.
//
// Idempotent : si le compte de test n'a jamais ete utilise (rien a
// supprimer), repond simplement avec des compteurs a zero, jamais une erreur.
//
// Portage Cloudflare Pages Functions : voir CLOUDFLARE_MIGRATION.md.
import { wrapVercelHandler } from "./_shim.js";
import * as lib from "./_verification-lib.js";

const TARGET_CANTON = "GE";
const TARGET_SLUG = "compte-test-legatis";

async function handler(req, res) {
  if (req.method !== "POST") {
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

  const filter = `canton=eq.${TARGET_CANTON}&avocat_slug=eq.${encodeURIComponent(TARGET_SLUG)}`;

  try {
    const [requests, accounts, submissions] = await Promise.all([
      lib.supabaseSelect("verification_requests", `${filter}&select=id,pending_user_id,document_path,selfie_path`),
      lib.supabaseSelect("lawyer_accounts", `${filter}&select=user_id`),
      lib.supabaseSelect("lawyer_profile_submissions", `${filter}&select=photo_path`),
    ]);

    await lib.storageDelete(requests.flatMap((r) => [r.document_path, r.selfie_path]));
    await lib.storageDelete(submissions.map((s) => s.photo_path), "lawyer-photos");

    if (requests.length) {
      await lib.supabaseDelete("verification_requests", filter);
    }

    const userIds = new Set([
      ...requests.map((r) => r.pending_user_id).filter(Boolean),
      ...accounts.map((a) => a.user_id).filter(Boolean),
    ]);
    for (const userId of userIds) {
      // Cascade : supprime aussi lawyer_accounts et lawyer_profile_submissions
      // lies a ce user_id (foreign keys "on delete cascade").
      await lib.adminDeleteUser(userId);
    }

    res.status(200).json({
      ok: true,
      deleted: {
        verification_requests: requests.length,
        auth_users: userIds.size,
        profile_submissions: submissions.length,
      },
    });
  } catch (err) {
    res.status(502).json({ error: "reset_failed", detail: String(err.message || err) });
  }
}

export const onRequest = wrapVercelHandler(handler);
