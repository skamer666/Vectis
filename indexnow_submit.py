#!/usr/bin/env python3
"""
Soumission d'URLs a IndexNow (protocole partage par Bing, Yandex, Seznam.cz,
Naver via api.indexnow.org). Script autonome, sans dependance externe
(urllib de la stdlib), volontairement separe de build.py : le build Vercel
ne doit jamais dependre d'un appel reseau sortant.

Usage :
    python3 indexnow_submit.py url1 url2 url3 ...
    echo -e "url1\nurl2" | python3 indexnow_submit.py -

La cle doit correspondre exactement a celle utilisee par gen_indexnow_key()
dans build.py (fichier de verification {cle}.txt a la racine du site).
"""
import json
import sys
import urllib.request

INDEXNOW_KEY = "7f3a9c14e8b5426a9d2f6c1e0a7b8d3f"
HOST = "legatis.ch"
KEY_LOCATION = f"https://{HOST}/{INDEXNOW_KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"

# Limite IndexNow : 10'000 URLs par requete.
BATCH_SIZE = 10000


def submit(urls):
    urls = [u for u in dict.fromkeys(urls) if u.strip()]
    if not urls:
        print("Aucune URL a soumettre.", file=sys.stderr)
        return 0
    total_ok = 0
    for i in range(0, len(urls), BATCH_SIZE):
        batch = urls[i:i + BATCH_SIZE]
        payload = json.dumps({
            "host": HOST,
            "key": INDEXNOW_KEY,
            "keyLocation": KEY_LOCATION,
            "urlList": batch,
        }).encode("utf-8")
        req = urllib.request.Request(
            ENDPOINT, data=payload, method="POST",
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                code = resp.getcode()
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:
            print(f"Erreur reseau IndexNow : {e}", file=sys.stderr)
            continue
        if code in (200, 202):
            print(f"IndexNow OK ({code}) : {len(batch)} URLs soumises.", file=sys.stderr)
            total_ok += len(batch)
        else:
            print(f"IndexNow reponse inattendue ({code}) pour {len(batch)} URLs.", file=sys.stderr)
    return total_ok


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["-"]:
        urls = [line.strip() for line in sys.stdin if line.strip()]
    else:
        urls = args
    n = submit(urls)
    print(f"{n} URLs soumises avec succes.", file=sys.stderr)
