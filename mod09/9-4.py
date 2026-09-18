# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
#  Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. 
# Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. 
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

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

autot =[]

for i in range(10):
    rekisteritunnus = f"ABC-{ i+ 1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

kilpa = True

while kilpa:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)

    for auto in autot:
        auto.kulje(1)

    for auto in autot:
        if auto.matka >= 10000:
            kilpa = False

print(f"{'Rekisteritunnus':<10} {'Huippunopeus':<15} {'Nopeus':<10} {'Matka':<10}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<15} {auto.nopeus:<10} {auto.matka:<10}")


