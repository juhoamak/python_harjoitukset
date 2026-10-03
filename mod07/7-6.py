# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle 
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

from math import pi

def laske_yksikköhinta(halkaisija, hinta):
    säde = halkaisija / 2
    pinta_ala = pi * säde ** 2
    pinta_ala_m2 = pinta_ala / 10000

    yksikköhinta = hinta / pinta_ala_m2

    return yksikköhinta

##pääohjelma

halkaisija1 = int(input("Syötä ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Syötä ensimmäisen pizzan hinta: "))
halkaisija2 = int(input("Syötä toisen pizzan halkaisija: "))
hinta2 = float(input("Syötä toisen pizzan hinta: "))

pizza1 = laske_yksikköhinta(halkaisija1,hinta1)
pizza2 = laske_yksikköhinta(halkaisija2,hinta2)

if pizza1 < pizza2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle!")
elif pizza2 < pizza1:
    print("Toinen pizza antaa paremman vastineen rahalle!")
else:
    print("Molemmat pizzat antavat saman vastineen rahalle.")

