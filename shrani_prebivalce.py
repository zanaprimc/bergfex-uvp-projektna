import requests

url = "https://en.wikipedia.org/wiki/List_of_European_countries_by_population"
headers = {'User-Agent': 'Mozilla/5.0'}

def shrani_stran(url):
    odgovor = requests.get(url, headers=headers)
    odgovor.raise_for_status()
    
    # shrani HTML v datoteko
    datoteka = f"prebivalci.html"
    with open(datoteka, 'w', encoding='utf-8') as f:
        f.write(odgovor.text)

if __name__ == '__main__':
    shrani_stran(url)
