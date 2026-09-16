# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

    # Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    # Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

suku_puoli = input("Syötä sukupuolesi: ")
hemo_globiini = int(input("Syötä hemoglobiiniarvosi (g/l): "))

if suku_puoli == "nainen" and 117 <= hemo_globiini <= 175:
    print("Sinulla on normaali hemoglobiiniarvo.")
elif suku_puoli == "nainen" and hemo_globiini < 117:
    print("Sinulla on alhainen hemoglobiiniarvo.")
elif suku_puoli == "nainen" and hemo_globiini > 175:
    print("Sinulla on korkea hemoglobiiniarvo.")
elif suku_puoli == "mies" and 134 <= hemo_globiini <= 195:
    print("Sinulla on normaali hemoglobiiniarvo.")
elif suku_puoli == "mies" and hemo_globiini < 134:
    print("Sinulla on alhainen hemoglobiiniarvo.")
elif suku_puoli == "mies" and hemo_globiini > 195:
    print("Sinulla on korkea hemoglobiiniarvo")
else:
    print("Virheellinen sukupuoli.")
