# Programa que pide al usuario un número entero y muestra por 
# pantalla un triángulo rectángulo de altura de el número introducido.

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")