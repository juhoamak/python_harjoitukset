# Class, object, constructor

#class Pelaaja:
    #def __init__(self, nimi, elamat=3, kolikot=0, pisteet=0 ):
        #self.nimi = nimi
        #self.elamat = elamat
       # self.kolikot = kolikot
       # self.pisteet = pisteet
       

#Pelaaja1 = Pelaaja("Mario")

#print(f"Nimi: {Pelaaja1.nimi}\nElämät: {Pelaaja1.elamat}\nKolikot: {Pelaaja1.kolikot}\nPisteet: {Pelaaja1.pisteet}")


# Merirosvolaiva-luokka, jonka ominaisuuksina ovat nimi, tykkien määrä, miehistön määrä ja kulta.
# Alustaja saa parametreina: laivan nimen, tykkien määrän ja miehistön määrän
# Uuden laivan kultamäärä asetetaan automaattisesti nollaksi.

class Merirosvolaiva:
    def __init__(self, nimi, tykit, miehistö, kulta=0):
        self.nimi = nimi
        self.tykit = tykit
        self.miehistö = miehistö
        self.kulta = kulta

    def loyda_aarre(self, maara):
        self.kulta = self.kulta + maara 
    def meneta_kultaa(self, maara):
        if self.kulta - maara >= 0:
            self.kulta = self.kulta - maara

# Pääohjelma
Merirosvolaiva1 = Merirosvolaiva("The Black Pearl", 12, 40)

Merirosvolaiva1.loyda_aarre(200)
Merirosvolaiva1.loyda_aarre(75)
Merirosvolaiva1.meneta_kultaa(100)

print(f"Nimi:{Merirosvolaiva1.nimi}\nTykit:{Merirosvolaiva1.tykit}")
print(f"Miehistö:{Merirosvolaiva1.miehistö}\nKulta:{Merirosvolaiva1.kulta}")    
        

