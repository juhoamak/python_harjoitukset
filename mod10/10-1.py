# Ohjelma jossa luotu hissi, joka metodien avulla siirtyy haluttuun kerrokseen

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

# pääohjelma

hissi1 = Hissi(1, 20)

hissi1.siirry_kerrokseen(5)

print(f"Kerros:{hissi1.kerros}")

hissi1.siirry_kerrokseen(1)

print(f"Kerros:{hissi1.kerros}")