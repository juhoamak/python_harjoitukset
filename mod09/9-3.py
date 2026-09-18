# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. 
#  Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.matka = self.matka + self.nopeus * tuntimaara
    


Auto1 = Auto("ABC-123", 142)

Auto1.kiihdytä(30)
Auto1.kiihdytä(70)
Auto1.kiihdytä(50)

Auto1.kulje(1.5)

print(f"Nopeus:{Auto1.nopeus}\nMatka:{Auto1.matka}")



Auto1.kiihdytä(-200)



# Pääohjelma
print(f"Rekisteritunnus:{Auto1.rekisteritunnus}\nHuippunopeus:{Auto1.huippunopeus}\nNopeus:{Auto1.nopeus}\nMatka:{Auto1.matka}")


    

