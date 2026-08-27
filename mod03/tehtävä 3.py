#ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

print("ohjelma kysyy suorakulmion kannan ja korkeuden ja tulostaa sen piirin ja pinta-alan.\n")

suorakulmio_kanta = input("Syötä suorakulmion kanta: ")

suorakulmio_korkeus = input("Syötä suorakulmion korkeus: ")

piiri = ((float(suorakulmio_kanta) * 2) + (float(suorakulmio_korkeus) * 2))

pinta_ala = (float(suorakulmio_korkeus) * float(suorakulmio_kanta))

print("Suorakulmion piiri: " + str(piiri))

print("Suorakulmion pinta-ala: " + str(pinta_ala))

