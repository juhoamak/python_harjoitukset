#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia: 

#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.

#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

print("Ohjelma arpoo ja tulostaa kaksi erilaista numerolukon koodia.\n")

import random

kolmenumeroinen_koodi = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)

nelinumeroinen_koodi = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

print("kolmenumeroinen koodi: " + str(kolmenumeroinen_koodi))

print("nelinumeroinen koodi: " + str(nelinumeroinen_koodi))

