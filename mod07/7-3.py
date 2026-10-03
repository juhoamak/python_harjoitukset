# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.


def gallonat_litroiksi(galloonat):
    litrat = galloonat * 3.785
    return litrat

galloonat = float(input("Syötä gallonat: "))

while galloonat >= 0:
    litrat = gallonat_litroiksi(galloonat)
    print(f"{litrat}, litraa")
    galloonat = float(input("Syötä gallonat: "))



