#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen 
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

print("Syötä kuhan pituus niin sinulle lasketaan onko se alamittainen.")

kuha_pituus = int(input("Syötä kuhan pituus: "))
if kuha_pituus < 37:
    print("Kuhasi on " + str(37 - kuha_pituus) + " senttiä alamittainen, heitä se takaisin järveen.")


