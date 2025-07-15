import os
import csv

# Poti do map in datotek
mapa_smucisca = 'smucisca_html'  # Pot do mape s HTML datotekami
csv_datoteka = 'smucisca.csv'      # Pot do CSV datoteke

# Preberemo imena smučišč iz mape (brez .html)
smucisca_v_mapi = {f[:-5] for f in os.listdir(mapa_smucisca) if f.endswith('.html')}

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
manjkajoca_smucisca = smucisca_v_mapi - smucisca_v_csv

# Izpis rezultatov
print("Smučišča, ki so v mapi, a ne v CSV datoteki:")
for smucisce in sorted(manjkajoca_smucisca):
    print(smucisce)

print(f"Skupaj: {len(manjkajoca_smucisca)} manjkajočih smučišč")


