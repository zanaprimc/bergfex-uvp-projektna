# bergfex-uvp-projektna
**Projektna naloga pri predmetu Uvod v Programiranje**

_Komentar prihodnjim študentskim bralcem:_ profesor Marc ni imel resnih pripomb glede strukture ter izvedbe, edino o čemer me je opozoril so moji dolgi komentarji ter vprašljivo humorni vložki znotraj kode. Izgleda, da projekt dosega standarde UVP.

V okviru te projektne naloge bom zbral podatke o ELO ratingu top 100 Šahistov od leta 2000 do leta 2024 ter analiziral nekatere prisotne trende.

## Navodila za uporabo
### Python ter git
Potreben pogoj za uspešno uporabo je nameščen Python ter git, po možnosti katero izmed novejših verzij.
### Nalaganje datotek
Da naložite vse potrebne datoteke za uporabo v ukazno vrstico napišite:
```console
git clone https://github.com/HugoTrebse/UVP-projektna-naloga.git
```
### Nameščanje knjižnjic
Potrebno je naložiti tudi nekaj knjižnjic. To storite v ukazni vrstici na naslednji način:
```console
pip install re requests csv os copy pandas matplotlib
```
### Uporaba programa:
Najprej se z ukazoma  ``` cd ``` ter ``` dir ``` orientirajte do mape, v kateri se nahajajo datoteke, ki smo jih naložili v prejšnjem koraku.
Nato poženite naslednji ukaz:
```console
python main.py
```
Na avtorjevem prenosniku se zbiranje podatkov, ki ga začnemo z zgornjim ukazom, konča v manj kot minuti.
### Dostop do analize podatkov
Analiza zbranih podatkov se nahaja v datoteki ```analiza_podatkov.ipynb```.
Datoteko lahko odpremo z poljubnim programom, ki je namenjen branju Jupyter Notebooka. Če takega programa nimate nameščenega, pa vam priporočam, da si končno obliko datoteko ogledate kar na githubu na [naslednjem linku](https://github.com/HugoTrebse/UVP-projektna-naloga/blob/main/analiza_podatkov.ipynb).


## TODO:
Last:
- Dodaj napise na grafih.
- Dodaj količino podatkov v uvod.
- Horizontal scrollbar problem.