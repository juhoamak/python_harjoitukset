# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def lukujen_summa(luvut):
    summa = 0

    for luku in luvut:
        summa = luku + summa

    return summa

luvut = [6,7,9,4,2]

summa = lukujen_summa(luvut)

print(summa)
