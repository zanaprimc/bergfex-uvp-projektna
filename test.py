import re

vzorec = re.compile(
    r'<title>.*?Skiing holiday (?P<ime>.+?)<\/title>.*?'
    r'"addressCountry":"(?P<drzava>\w+)".*?'
    r'(<span[^>]*>\s*(?P<nadmorska>\d+\.?\d*(?:\s-\s\d+\.?\d*)?)\s*m\s*</span>.*?)?',
    # r'<span[^>]*>\s*(?P<dolzina>\d+[\.]?\d*)\s*km\s*</span>.*?'
    # r'(?P<valuta>€|CHF|BAM|CZK|PLN)?\s*(?P<cena>\d+[\,]\d+|n/a|dynamic)\b',
    re.IGNORECASE | re.DOTALL
)

def izlusci_podatke_o_smuciscu(smucisce):
    
    with open(f"smucisca_html/{smucisce}.html", 'r', encoding='utf-8') as dat:
        besedilo = dat.read()
        for najdba in re.finditer(vzorec, besedilo):
            print(najdba["ime"])
            print(najdba["drzava"])

            if not najdba["nadmorska"]:
                nadmorska = "n/a"
            else:
                nadmorska = najdba["nadmorska"]
            
            print(nadmorska)

        #     print(najdba["dolzina"])
        #     print(najdba["cena"])

if __name__ == '__main__':
    izlusci_podatke_o_smuciscu("fischenthal")

