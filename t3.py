import math
import random


a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
cant = int(input("Ingrese la cantidad de puntos: "))

elipse = 0
interseccion = 0


for i in range(cant):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)

   
    en_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1

   
    en_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1

    
    if en_elipse:
        elipse = elipse + 1
        if en_hiperbola:
            interseccion = interseccion + 1


area_elipse = math.pi * a * b


if elipse > 0:
    area_interseccion = (interseccion / elipse) * area_elipse
else:
    area_interseccion = 0


print("\n--- RESULTADOS ---")
print("Puntos en la elipse:", elipse)
print("Puntos en la intersección:", interseccion)
print(f"Area de la elipse: {area_elipse:.4f}")
print(f"Area aproximada de la interseccion: {area_interseccion:.4f}")