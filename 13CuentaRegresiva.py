# Programa que pide al usuario un número entero positivo
#  y muestra por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")

# Mejora by Continue
print("\n")

while True:
    n = int(input("Introduce un número entero positivo: "))
    if n >= 0:
        for i in range(n, -1, -1):
            print(i, end=", ")
        break
    else:
        print("El número debe ser positivo, intenta de nuevo.")

# Mejora by Continue
print("\n")
try:
    n = int(input("Introduce un número entero positivo: "))
    if n < 0:
        raise ValueError("El número debe ser positivo")
    countdown = ", ".join(str(i) for i in range(n, -1, -1))
    print(countdown)
except ValueError as e:
    print(e)