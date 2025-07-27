import requests
import os

drzave = ["andorra",
          "deutschland", 
          "slovenia", 
          "kroatien", 
          "oesterreich", 
          "schweiz",
          "italien",
          "frankreich",
          "nederland",
          "belgie",
          "polska",
          "liechtenstein",
          "czechia",
          "slovakia",
          "spanien",
          "bosnien-herzegowina"]

def shrani_html(drzave):
    for drzava in drzave:
        folder = f"bergfex_html/{drzava}" # mapo bergfex_html imam že ustvarjeno
        os.makedirs(folder)
        
        page = 1
        while True:
            url = f"https://www.bergfex.com/{drzava}/?page={page}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            
            try:
                print(f"Pridobivam: {url}")
                odgovor = requests.get(url, headers=headers)
                odgovor.raise_for_status()
                
                # shrani HTML v datoteko
                datoteka = f"{folder}/page_{page}.html"
                with open(datoteka, 'w', encoding='utf-8') as f:
                    f.write(odgovor.text)
                print(f"Shranjeno v {datoteka}")
                
                page += 1
                
            except Exception as e:
                print(f"Napaka pri {drzava}, stran {page}: {str(e)}")
                break

