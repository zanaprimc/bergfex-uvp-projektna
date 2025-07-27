# bergfex-uvp-projektna
**Projektna naloga pri predmetu Uvod v Programiranje**

V okviru te projektne naloge bom pridobila podatke o evropskih smučiščih ter analizirala njihove karakteristike v povezavi z državo, v kateri ležijo.

## Navodila za uporabo
### Python ter git
Pogoj za  uporabo je nameščen Python ter git.
### Nalaganje datotek
Da naložite vse potrebne datoteke za uporabo v ukazno vrstico napišite:
```console
git clone https://github.com/zanaprimc/bergfex-uvp-projektna.git 
```
### Nameščanje knjižnjic
Potrebno je naložiti tudi nekaj knjižnic. To storite v ukazni vrstici na naslednji način:
```console
pip install re requests csv os pandas matplotlib.pyplot IPython.display geopandas contextily numpy
```
### Uporaba programa:
Najprej se z ukazoma  ``` cd ``` ter ``` dir ``` premaknite do mape, v kateri se nahajajo datoteke, ki smo jih naložili v predprejšnjem koraku.
Nato poženite naslednji ukaz:
```console
python main.py
```
Če ukaza ne poženete, se uporabita že priloženi csv datoteki s podatki, pridobljenimi dne 27. 7. 2025.

### Dostop do analize podatkov
Analiza zbranih podatkov se nahaja v datoteki ```analiza.ipynb```.