import re
import os
import requests

datoteke = []
start_poti = "bergfex_html"

for koren, folder, dokumenti in os.walk(start_poti):
    for dokument in dokumenti:
        if dokument.endswith(".html"):
            pot = os.path.join(koren, dokument)
            datoteke.append(pot)

smucisca = []
vzorec = r'<a href="/(?P<interno_ime>.+)/" target="_blank"'

for datoteka in datoteke:
    with open(datoteka) as dat:
        besedilo = dat.read()
        for najdba in re.finditer(vzorec, besedilo):
            smucisca.append(najdba["interno_ime"])

# s = set()
# duplikati = []
# for smucisce in smucisca:
#     if smucisce in s:
#         duplikati.append(smucisce)
#     else:
#         s.add(smucisce)
# print(duplikati)

# print(len(smucisca))
# print(len(s))

# Ugotovim, da se dolzina seznama (ko odstranim podvojene elemente) spremeni iz 2210 v 2190, torej obstaja 20 podvojenih smucisc, 
# ki si jih "delita" dve ali vec drzav (npr. Avoriaz med Francijo in Švico), oz. so nekatera poljska smucisca navedena veckrat.
# Ker je to zanemarljiv delez, ohranim nakljucno drzavo, ki si "lasti" smucisce, torej v analizi zatajim dvojno lastnistvo.

def shrani_html(smucisca):
    for smucisce in smucisca:
        url = f"https://www.bergfex.com/{smucisce}/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        odgovor = requests.get(url, headers=headers)

        if odgovor.status_code != 200:
            print("Napaka", smucisce)
            continue

        else:
            with open(os.path.join("smucisca_html", f"{smucisce}.html"), "w") as dat:
                dat.write(odgovor.text)

if __name__ == '__main__':
    shrani_html(smucisca)