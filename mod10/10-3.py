# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. 
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        print(self.kerros)

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print(self.kerros)

    def siirry_kerrokseen(self,kohde):
        while self.kerros < kohde:
            self.kerros_ylös()

        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alakerta, yläkerta, hissi_maara):
        self.alakerta = alakerta
        self.yläkerta = yläkerta
        self.hissit = []
        self.hissi_maara = hissi_maara

        for i in range(hissi_maara):
            hissi = Hissi(alakerta, yläkerta)
            self.hissit.append(hissi)

    

    def aja_hissiä(self, hissi_numero, kohdekerros):
        hissi = self.hissit[hissi_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alakerta)



##Pääohjelma

Talo1 = Talo(1,12,2)
Talo1.aja_hissiä(2, 7)
Talo1.palohalytys()
