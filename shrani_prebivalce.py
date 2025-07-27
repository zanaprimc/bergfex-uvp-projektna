import requests

headers = {'User-Agent': 'Mozilla/5.0'}

def shrani_stran(url):
    odgovor = requests.get(url, headers=headers)
    odgovor.raise_for_status()
    
    # shrani HTML v datoteko
    datoteka = f"prebivalci.html"
    with open(datoteka, 'w', encoding='utf-8') as f:
        f.write(odgovor.text)

