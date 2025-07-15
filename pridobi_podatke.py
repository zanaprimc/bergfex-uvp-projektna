import re
import os

vzorec = re.compile(
    r'<title>.*?Skiing holiday (?P<ime>.+?)<\/title>.*?'
    r'"addressCountry":"(?P<drzava>\w+)".*?'
    r'<span[^>]*>\s*(?P<nadmorska>\d+\s-\s\d+)\s*m\s*</span>.*?'
    r'<span[^>]*>\s*(?P<dolzina>\d+[\.]?\d*)\s*km\s*</span>.*?'
    r'(?P<valuta>€|CHF|BAM|CZK|PLN)?\s*(?P<cena>\d+[\,]\d+|n/a|dynamic)\b',
    re.IGNORECASE | re.DOTALL
)

def izlusci_podatke_o_smuciscih(start_poti):
    smucisca_info = []
    
    for koren, folder, dokumenti in os.walk(start_poti):
        for dokument in dokumenti:
            pot = os.path.join(koren, dokument)

            with open(pot) as dat:
                besedilo = dat.read()
                for najdba in re.finditer(vzorec, besedilo):

                    if not najdba["valuta"]:
                        valuta = "n/a"
                    else:
                        valuta = najdba["valuta"]

                    info = {
                        "interno_ime": dokument[:-5],
                        "smucisce": najdba["ime"],
                        "drzava": najdba["drzava"],
                        "nadmorska_visina": najdba["nadmorska"],
                        "km_prog": najdba["dolzina"],
                        "karta": najdba["cena"],
                        "valuta": valuta
                        }
                    
                    smucisca_info.append(info)

    # print(len(smucisca_info))
    return smucisca_info

if __name__ == '__main__':
    izlusci_podatke_o_smuciscih("smucisca_html")