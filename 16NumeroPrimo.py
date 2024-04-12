# Programa que pide al usuario un número entero y muestra por pantalla si es un número primo o no.

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

# Mejora by Continue

print("\n")
while True:
    n = int(input("Introduce un número entero positivo mayor que 2: "))
    i = 2
    while n % i != 0:
        i += 1
    if i == n:
        print(str(n) + " es primo")
    else:
        print(str(n) + " no es primo")

    repetir = input("¿Deseas evaluar otro número? (s/n): ")
    if repetir.lower() != 's':
        break