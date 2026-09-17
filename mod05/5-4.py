# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
luku_arvaus = float(input("Arvaa luku: "))

oikea_luku = random.randint(1, 10)

while luku_arvaus != oikea_luku:
    if luku_arvaus < oikea_luku:
        print("Liian pieni arvaus")
    elif luku_arvaus > oikea_luku:
        print("Liian suuri arvaus") 
    
    luku_arvaus = float(input("Arvaa luku: "))

print("Oikein.")


