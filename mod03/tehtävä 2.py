#Ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan

import math

print("Tämä ohjelma kysyy ympyrän säteen ja tulostaa sen pinta-alan.\n")
ympyrä_säde = input("Syötä ympyrän säde: ")

pinta_ala = ((float(ympyrä_säde) * float(ympyrä_säde)) * math.pi)

print("Pinta_ala: " + str(pinta_ala))
