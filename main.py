import csv
import pridobi_podatke

imena_polj = ["interno_ime", "smucisce", "drzava", "nadmorska_visina", "km_prog", "karta", "valuta"]

start_poti = "smucisca_html"
smucisca_info = pridobi_podatke.izlusci_podatke_o_smuciscih(start_poti)

with open("smucisca.csv", mode="w", newline="") as dat:
    writer = csv.DictWriter(dat, fieldnames=imena_polj)
    writer.writeheader()
    writer.writerows(smucisca_info)