#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

print("ohjelma, joka kysyy kolme kokonaislukua.\n Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.\n")

int_1 = input("Syötä kokonaisluku: ")

int_2 = input("Syötä kokonaisluku: ")

int_3 = input("Syötä kokonaisluku: ")

Summa = (int(int_1) + int(int_2) + int(int_3))

Tulo = (int(int_1) * int(int_2) * int(int_3))

keskiarvo = ((int(int_1) + int(int_2) + int(int_3)) / 3)

print("Lukujen summa: " + str(Summa))
print("Lukujen tulo: " + str(Tulo))
print("Lukujen keskiarvo: " + str(keskiarvo))


