# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

maksimi_luku = int(input("Syötä maksimisilmäluku: "))

# funktio

def silmaluku(tahkot):
    heitto = random.randint(1, tahkot)
    return heitto

# Pääohjelma

heitto = 0

while heitto != maksimi_luku:
    heitto = silmaluku(maksimi_luku)
    print(heitto)
