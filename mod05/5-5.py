# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

user = input("Syötä käyttäjänimi: ")
password = input("Syötä salasana: ")
tries = 1

while user != "python" or password != "rules":
    if tries == 5:
        print("Pääsy evätty.")
        break
    user = input("Syötä käyttäjänimi: ")
    password = input("Syötä salasana: ")
    tries = tries + 1

if user == "python" and password == "rules":
    print("Tervetuloa!")

    