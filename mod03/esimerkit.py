# Muuttujat ja vuorovaikutteiset ohjelmat

# Ohjelma joka kysyy käyttäjältä lämpötilan Fahrenheit asteina
# Muuttaa sen Celsiukseen

# print("Tämä ohjelma muuntaa fahrenheitit celsius asteiksi.\n")
# fahrenheit = input("Anna lämpötila Fahrenheit yksikössä: ")

# celsius = (float(fahrenheit) - 32) * 5 / 9

# print("Konversion tulos: " + str(celsius))

# import math

# pii_luku = math.pi

# print(f"{'pii':12s}:{pii_luku:10.5f}")
import math

Radius = input("Enter radius of the circle: ")

Side_length = input("Enter side length of the square: ")

Area_circle = ((float(Radius) * float(Radius)) * math.pi)

Area_square = (float(Side_length) * float(Side_length))

print("Area of the circle: " + str(Area_circle))

print("Area of the square: " + str(Area_square))

