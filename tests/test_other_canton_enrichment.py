"""
Rattachement du cache de decouverte "autres cantons" (data/domaines_autres_cantons.json)
aux etudes des cantons generiques (ZH, BS, SG, GR, LU, ...). Ces CSV sources n'ont pas de
colonne site_web -- contrairement a Geneve/Vaud, le rattachement se fait par nom de
cabinet (firm_core_name) plutot que par domaine. Le point critique a tester est le
garde-fou anti-collision : mieux vaut rater un rattachement que se tromper de cabinet.
"""
import build


def test_firm_core_name_strips_legal_suffix_and_matches_variants():
    assert build.firm_core_name("Schellenberg Wittmer AG") == build.firm_core_name("Schellenberg Wittmer Ltd")
    assert build.firm_core_name("Bratschi SA") == build.firm_core_name("Bratschi AG")


def test_firm_core_name_does_not_collapse_distinct_firms():
    assert build.firm_core_name("Meyer Legal AG") != build.firm_core_name("Meyer & Kunz AG")


def test_attach_name_based_enrichment_matches_unique_firm():
    canton_data = {
        "ZH": {"firms": [{"etude": "Exemple Avocats AG", "members": []}]},
    }
    entries = [{"canton": "ZH", "firm_name": "Exemple Avocats Ltd", "founding_year": 1990}]
    attached, skipped = build.attach_name_based_enrichment(canton_data, entries)
    assert attached == 1
    assert skipped == 0
    assert canton_data["ZH"]["firms"][0]["_name_web"]["founding_year"] == 1990


def test_attach_name_based_enrichment_skips_ambiguous_collision():
    # Deux etudes distinctes du meme canton partagent le meme nom "coeur" une
    # fois la forme juridique retiree : on ne doit rattacher a aucune des deux.
    canton_data = {
        "ZH": {"firms": [
            {"etude": "Meyer Avocats AG", "members": []},
            {"etude": "Meyer Avocats SA", "members": []},
        ]},
    }
    entries = [{"canton": "ZH", "firm_name": "Meyer Avocats Ltd", "founding_year": 2000}]
    attached, skipped = build.attach_name_based_enrichment(canton_data, entries)
    assert attached == 0
    assert skipped == 1
    assert "_name_web" not in canton_data["ZH"]["firms"][0]
    assert "_name_web" not in canton_data["ZH"]["firms"][1]


def test_attach_name_based_enrichment_ignores_other_cantons():
    canton_data = {
        "ZH": {"firms": [{"etude": "Exemple Avocats AG", "members": []}]},
        "BS": {"firms": [{"etude": "Exemple Avocats AG", "members": []}]},
    }
    entries = [{"canton": "ZH", "firm_name": "Exemple Avocats AG", "founding_year": 1990}]
    attached, skipped = build.attach_name_based_enrichment(canton_data, entries)
    assert attached == 1
    assert "_name_web" not in canton_data["BS"]["firms"][0]


def test_load_other_canton_enrichment_drops_failed_and_cantonless_entries():
    entries = build.OTHER_CANTON_ENRICHMENT
    assert all(e.get("canton") for e in entries)
    assert all(e.get("firm_name") for e in entries)


def test_real_cache_produces_matches_without_ambiguity_errors():
    # Regression : au moment d'ecrire ce test, le cache reel produit des
    # rattachements et au plus quelques collisions ignorees -- jamais zero
    # rattachement (signe que le format du cache ou le matching aurait casse).
    assert build._name_matches_attached > 0


def test_web_practice_areas_falls_back_to_fr_then_en():
    # Regression (audit du 2026-09-04) : les cabinets dont le site officiel
    # scrape est nativement en anglais n'ont que practice_areas_en de rempli
    # -- practice_areas_fr/de/it n'ont jamais ete traduits pour ces entrees.
    # Un lookup direct par langue renvoyait [] pour fr/de/it malgre une
    # donnee reelle disponible en cache (528 fiches avocat concernees).
    web_en_only = {"practice_areas_fr": [], "practice_areas_de": [], "practice_areas_it": [],
                   "practice_areas_en": ["Employment Law", "Tax Law"]}
    assert build.web_practice_areas(web_en_only, "fr") == ["Employment Law", "Tax Law"]
    assert build.web_practice_areas(web_en_only, "de") == ["Employment Law", "Tax Law"]
    assert build.web_practice_areas(web_en_only, "it") == ["Employment Law", "Tax Law"]
    assert build.web_practice_areas(web_en_only, "en") == ["Employment Law", "Tax Law"]


def test_web_practice_areas_prefers_requested_lang_over_fallback():
    web_fr = {"practice_areas_fr": ["Droit du travail"], "practice_areas_de": ["Arbeitsrecht"],
              "practice_areas_en": ["Employment law"]}
    assert build.web_practice_areas(web_fr, "de") == ["Arbeitsrecht"]


def test_web_practice_areas_empty_when_nothing_available():
    assert build.web_practice_areas({"practice_areas_fr": []}, "fr") == []
    assert build.web_practice_areas(None, "fr") == []
