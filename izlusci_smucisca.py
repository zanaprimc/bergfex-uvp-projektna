import re
import os

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

print(len(smucisca))
