import izlusci_smucisca
import csv

start_poti = "bergfex_html"
smucisca = izlusci_smucisca.printaj_smucisca(start_poti)

mn = set()
for el in smucisca:
    mn.add(el)

print(len(mn))

# Poti do map in datotek
csv_datoteka = 'smucisca.csv'      # Pot do CSV datoteke

# Preberemo imena smučišč iz CSV datoteke (prvi stolpec)
smucisca_v_csv = set()
try:
    with open(csv_datoteka, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:  # Če vrstica ni prazna
                smucisca_v_csv.add(row[0].strip())
except FileNotFoundError:
    print(f"Opozorilo: Datoteka {csv_datoteka} ne obstaja. Vse datoteke v mapi bodo izpisane.")

# Najdemo smučišča, ki so v mapi, a ne v CSV
print(len(smucisca_v_csv))
manjkajoca_smucisca = mn - smucisca_v_csv

# Izpis rezultatov
print("Smučišča, ki so v mapi, a ne v CSV datoteki:")
for smucisce in sorted(manjkajoca_smucisca):
    print(smucisce)


