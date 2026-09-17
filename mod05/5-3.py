# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = input("syötä luku: ")
eka_luku = True

while luku != "":
    print(luku)
    luku = float(luku)
    if eka_luku:
        pienin = luku
        suurin = luku
        eka_luku = False
    else:
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

    luku = input("syötä luku: ")
    

print(f"Pienin: {pienin}")
print(f"Suurin: {suurin}")






