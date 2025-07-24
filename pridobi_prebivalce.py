import re

def shrani_stevilo(drzave):
    drzave_info = []
    with open("prebivalci.html", "r", encoding='utf-8') as dat:
        besedilo = dat.read()
        for slovar in drzave:
            for drzava, kratica in slovar.items():
                podatki = {}
                vzorec = re.compile(rf'<a[^>]*>{re.escape(drzava)}</a>\s*</td>\s*<td>(?P<stevilo>[\d,]+)</td>')
                for najdba in re.finditer(vzorec, besedilo):
                    podatki = {
                        "drzava": kratica,
                        "st_prebivalcev": najdba["stevilo"].replace(',', '') # odstranim vejice
                        }
                    drzave_info.append(podatki)
    
    return drzave_info