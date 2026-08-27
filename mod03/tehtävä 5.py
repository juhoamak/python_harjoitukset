#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.

#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.

#Yksi naula on 32 luotia.

#Yksi luoti on 13,3 grammaa.

print("Tämä ohjelma kysyy keskiaikaiset mitat ja laskee niiden massan nykymitoissa.\n")

luoti = 13.3

naula = 32 * luoti

leiviskä = 20 * naula

anna_naula = input("syötä naulat: ")

anna_leiviskä = input("syötä leiviskät: ")

anna_luoti = input("syötä luodit: ")

massa = (float(anna_leiviskä) * float(leiviskä)) + (float(anna_luoti) * float(luoti)) + (float(anna_naula) * float(naula))

kilogrammat = massa // 1000

grammat = massa % 1000

print(("Massa nykymittojen mukaan.\n") + str(kilogrammat) + " kilogrammaa " + " ja " + (f"{grammat:.2f} grammmaa"))

