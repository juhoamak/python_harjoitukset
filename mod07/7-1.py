# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

# funktio

def silmaluku():
    heitto = random.randint(1,6)
    return heitto

# Pääohjelma

heitto = 0

while heitto != 6:
    heitto = silmaluku()
    print(heitto)






