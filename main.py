import csv
import shrani_imena
import shrani_prebivalce
import izlusci_smucisca
import pridobi_podatke
import pridobi_prebivalce

# SMUCISCA

imena_polj = ["interno_ime", "smucisce", "drzava", "nadmorska_visina", "km_prog", "karta", "valuta"]

start_poti = "smucisca_html"
smucisca_info = pridobi_podatke.izlusci_podatke_o_smuciscih(start_poti)

with open("smucisca.csv", mode="w", newline="") as dat:
    writer = csv.DictWriter(dat, fieldnames=imena_polj)
    writer.writeheader()
    writer.writerows(smucisca_info)

# STEVILO PREBIVALCEV

drzave = [{"Andorra": "AD"},
          {"Germany": "DE"}, 
          {"Slovenia": "SI"}, 
          {"Croatia": "HR"}, 
          {"Austria": "AT"}, 
          {"Czech Republic": "CZ"},
          {"Italy": "IT"},
          {"France": "FR"},
          {"Netherlands": "NL"},
          {"Belgium": "BE"},
          {"Poland": "PL"},
          {"Liechtenstein": "LI"},
          {"Switzerland": "CH"},
          {"Slovakia": "SK"},
          {"Spain": "ES"},
          {"Bosnia and Herzegovina": "BA"}]

imena_polj = ["drzava", "st_prebivalcev"]

drzave_info = pridobi_prebivalce.shrani_stevilo(drzave)

with open("prebivalci.csv", mode="w", newline="") as dat:
    writer = csv.DictWriter(dat, fieldnames=imena_polj)
    writer.writeheader()
    writer.writerows(drzave_info)