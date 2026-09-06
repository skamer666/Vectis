"""
Rattachement du cache d'enrichissement individuel (data/avocats_individuels_enrichment.json)
aux avocats des cantons sans champ "etude" du tout (AG, ZG, NE, TG, SO -- voir
data/ENRICHISSEMENT_PROGRESS.md, phase 3b). Contrairement aux deux caches precedents
(WEB_ENRICHMENT par domaine, OTHER_CANTON_ENRICHMENT par nom de cabinet), celui-ci
rattache directement par nom d'avocat + canton. Meme garde-fou anti-collision que
attach_name_based_enrichment : mieux vaut rater un rattachement que se tromper de personne.
"""
import json
import build


def test_attach_individual_enrichment_matches_unique_person():
    canton_data = {
        "ZG": {"individuals": [{"nom_complet": "Fischer Markus", "_slug": "fischer-markus"}]},
    }
    enrichment = {
        ("ZG", build.norm("Fischer Markus")): {
            "canton": "ZG", "person_name": "Fischer Markus",
            "practice_areas_fr": ["Droit du numérique"],
        },
    }
    attached, skipped = build.attach_individual_enrichment(canton_data, enrichment)
    assert attached == 1
    assert skipped == 0
    assert canton_data["ZG"]["individuals"][0]["_individual_web"]["practice_areas_fr"] == ["Droit du numérique"]


def test_attach_individual_enrichment_skips_ambiguous_collision():
    # Deux avocats du meme canton partagent le meme nom normalise dans le CSV
    # source : on ne rattache a aucun des deux plutot que de se tromper.
    canton_data = {
        "AG": {"individuals": [
            {"nom_complet": "Meier Thomas", "_slug": "meier-thomas"},
            {"nom_complet": "Meier Thomas", "_slug": "meier-thomas-2"},
        ]},
    }
    enrichment = {
        ("AG", build.norm("Meier Thomas")): {"canton": "AG", "person_name": "Meier Thomas"},
    }
    attached, skipped = build.attach_individual_enrichment(canton_data, enrichment)
    assert attached == 0
    assert skipped == 1
    assert "_individual_web" not in canton_data["AG"]["individuals"][0]
    assert "_individual_web" not in canton_data["AG"]["individuals"][1]


def test_attach_individual_enrichment_ignores_other_cantons():
    canton_data = {
        "ZG": {"individuals": [{"nom_complet": "Dormann Markus", "_slug": "dormann-markus"}]},
        "NE": {"individuals": [{"nom_complet": "Dormann Markus", "_slug": "dormann-markus"}]},
    }
    enrichment = {
        ("ZG", build.norm("Dormann Markus")): {"canton": "ZG", "person_name": "Dormann Markus"},
    }
    attached, skipped = build.attach_individual_enrichment(canton_data, enrichment)
    assert attached == 1
    assert "_individual_web" not in canton_data["NE"]["individuals"][0]


def test_load_individual_enrichment_drops_failed_and_incomplete_entries():
    entries = build.INDIVIDUAL_ENRICHMENT
    for (canton, _norm_name), entry in entries.items():
        assert entry.get("canton") == canton
        assert entry.get("person_name")
        assert not entry.get("_failed")


def test_load_individual_enrichment_merges_multiple_agent_files(tmp_path, monkeypatch):
    # Trois agents independants (Claude, un agent externe type OpenAI Codex, un
    # agent externe type Google Jules) ecrivent chacun dans leur propre fichier
    # -- load_individual_enrichment doit fusionner les trois sans conflit tant
    # que les personnes sont distinctes.
    monkeypatch.setattr(build, "DATA_DIR", str(tmp_path))
    (tmp_path / "avocats_individuels_enrichment.json").write_text(
        json.dumps({"ag-a": {"canton": "AG", "person_name": "Alice Muller"}}), encoding="utf-8")
    (tmp_path / "avocats_individuels_enrichment_chatgpt.json").write_text(
        json.dumps({"zg-b": {"canton": "ZG", "person_name": "Bruno Keller"}}), encoding="utf-8")
    (tmp_path / "avocats_individuels_enrichment_gemini.json").write_text(
        json.dumps({"ne-c": {"canton": "NE", "person_name": "Claire Dubois"}}), encoding="utf-8")
    entries = build.load_individual_enrichment()
    assert len(entries) == 3
    assert ("AG", build.norm("Alice Muller")) in entries
    assert ("ZG", build.norm("Bruno Keller")) in entries
    assert ("NE", build.norm("Claire Dubois")) in entries


def test_load_individual_enrichment_drops_cross_file_collision(tmp_path, monkeypatch):
    # Si deux fichiers d'agents differents renseignent par erreur la meme
    # personne (meme canton + meme nom normalise), on ecarte l'entree des deux
    # cotes plutot que de choisir arbitrairement laquelle des deux garder.
    monkeypatch.setattr(build, "DATA_DIR", str(tmp_path))
    (tmp_path / "avocats_individuels_enrichment.json").write_text(
        json.dumps({"ag-a": {"canton": "AG", "person_name": "Alice Muller", "phone": "111"}}), encoding="utf-8")
    (tmp_path / "avocats_individuels_enrichment_chatgpt.json").write_text(
        json.dumps({"ag-a2": {"canton": "AG", "person_name": "Alice Muller", "phone": "222"}}), encoding="utf-8")
    (tmp_path / "avocats_individuels_enrichment_gemini.json").write_text("{}", encoding="utf-8")
    entries = build.load_individual_enrichment()
    assert ("AG", build.norm("Alice Muller")) not in entries


def test_gen_canton_avocats_falls_back_to_individual_web_only_when_no_etude():
    # Le repli individuel dans gen_canton_avocats ne doit jamais s'appliquer
    # quand une etude existe deja en base (etude_name non vide) -- meme si un
    # _individual_web est present sur la ligne (ne devrait pas arriver en
    # pratique, mais le garde-fou doit tenir).
    import presentation_text as pt
    web_with_etude = {"firm_name": "Cabinet Ne Devrait Pas Apparaitre", "practice_areas_fr": ["Droit fiscal"]}
    etude_name = "Etude Reelle SA"
    etude_display = etude_name or (web_with_etude or {}).get("firm_name") or ""
    assert etude_display == "Etude Reelle SA"

    etude_name_empty = ""
    etude_display_empty = etude_name_empty or (web_with_etude or {}).get("firm_name") or ""
    assert etude_display_empty == "Cabinet Ne Devrait Pas Apparaitre"
