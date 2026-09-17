# Class, objeect, constructor

class Hero:
    def __init__(self, nimi, tyyppi, voima, huudahdus="Hei!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.huudahdus = huudahdus 



hero1 = Hero("Reinhardt", "Tankki", "Voimakas", "AAAAAAARGHH")
hero2 = Hero("Tracer", "DPS", "Nopea")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hän on {hero1.voima}, hän sanoo {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hän on {hero2.voima}, hän sanoo {hero2.huudahdus}")





