# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = float(input("Syötä tuumat: "))

while tuumat >= 0:
    senttimetrit = tuumat * 2.54
    print(senttimetrit)
    tuumat = float(input("Syötä tuumat: "))

