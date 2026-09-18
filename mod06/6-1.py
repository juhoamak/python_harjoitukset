# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

arpakuutiot = int(input("Syötä arpakuutioiden määrä: "))

summa = 0

for toisto in range(arpakuutiot):
    silmaluku = random.randint(1, 6)
    summa = silmaluku + summa

print("silmälukujen summa on:", summa)