"""
Regroupement des avocats fribourgeois par domaine d'email (Fribourg n'a ni champ
"etude" ni "site_web" dans son registre source, mais un champ email rempli a 100%
dont le domaine est presque toujours celui du cabinet). Generalisation de
derive_domain_firms(), deja utilise pour Vaud via site_web. Le point critique a
tester : les fournisseurs mail grand public (bluewin.ch, gmail.com...) ne doivent
jamais etre traites comme un cabinet, meme partages par plusieurs avocats.
"""
import build


def test_email_domain_extracts_domain():
    assert build.email_domain("v.emery@emery-avocats.ch") == "emery-avocats.ch"
    assert build.email_domain("  Info@Cabinet.CH ") == "cabinet.ch"
    assert build.email_domain("") is None
    assert build.email_domain("pas-un-email") is None


def test_derive_domain_firms_groups_by_email_domain():
    individuals = [
        {"etude": "", "email": "a@cabinet-x.ch", "ville": "Fribourg"},
        {"etude": "", "email": "b@cabinet-x.ch", "ville": "Fribourg"},
        {"etude": "", "email": "c@solo-lawyer.ch", "ville": "Bulle"},
    ]
    firms = build.derive_domain_firms(
        individuals, domain_fn=lambda r: build.email_domain(r.get("email")),
        excluded_domains=build.GENERIC_EMAIL_DOMAINS,
    )
    assert len(firms) == 1
    assert len(firms[0]["members"]) == 2
    # L'avocat seul sur son domaine (solo-lawyer.ch, non confirme ailleurs) ne
    # forme pas une "etude" -- reste liste comme independant.
    assert individuals[2]["etude"] == ""


def test_generic_email_providers_never_become_a_firm():
    individuals = [
        {"etude": "", "email": "a@bluewin.ch", "ville": "Fribourg"},
        {"etude": "", "email": "b@bluewin.ch", "ville": "Fribourg"},
        {"etude": "", "email": "c@bluewin.ch", "ville": "Fribourg"},
        {"etude": "", "email": "d@gmail.com", "ville": "Bulle"},
        {"etude": "", "email": "e@gmail.com", "ville": "Bulle"},
    ]
    firms = build.derive_domain_firms(
        individuals, domain_fn=lambda r: build.email_domain(r.get("email")),
        excluded_domains=build.GENERIC_EMAIL_DOMAINS,
    )
    assert firms == []
    assert all(r["etude"] == "" for r in individuals)


def test_fribourg_wired_into_canton_data_without_touching_other_cantons():
    fr = build.CANTON_DATA["FR"]
    assert len(fr["firms"]) > 0
    # Aucun des cabinets derives n'a un nom qui est en realite un fournisseur
    # mail grand public.
    slugified_generic = {build.slugify(d) for d in build.GENERIC_EMAIL_DOMAINS}
    assert not any(f["_slug"] in slugified_generic for f in fr["firms"])
    # Un canton non touche par ce mecanisme (ex. Neuchatel, toujours sans
    # aucun signal de regroupement) reste inchange : que des independants.
    ne = build.CANTON_DATA["NE"]
    assert len(ne["firms"]) == 0
