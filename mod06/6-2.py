#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []

luku = input("Syötä luku: ")
while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Syötä luku: ")

luvut.sort(reverse=True)

print(luvut[:5])
