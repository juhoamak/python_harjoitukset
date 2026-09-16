#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

   # LUX on parvekkeellinen hytti yläkannella.
   # A on ikkunallinen hytti autokannen yläpuolella.
   # B on ikkunaton hytti autokannen yläpuolella.
   # C on ikkunaton hytti autokannen alapuolella.

#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
print("Hyttiluokan kuvaus\n")

hytti_luokka = input("Syötä hyttiluokkasi: ")
if hytti_luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti_luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti_luokka == "B":
    print("B on ikkunallinen hytti autokannen yläpuolella.")
elif hytti_luokka == "C":
    print("C on ikkunallinen hytti autokannen yläpuolella.")
else:
    print("Virheellinen hyttiluokka!")

