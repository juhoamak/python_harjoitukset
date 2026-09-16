# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä. 
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosiluku = int(input("Syötä vuosiluku: "))

if vuosiluku % 400 == 0:
    print("vuosi on karkausvuosi!")
elif vuosiluku % 100 == 0:
    print("Vuosi ei ole karkausvuosi..")
elif vuosiluku % 4 == 0:
    print("Vuosi on karkausvuosi!")
else:
    print("Vuosi ei ole karkausvuosi..")




