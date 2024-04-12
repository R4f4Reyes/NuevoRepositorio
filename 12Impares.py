# Programa que pidr al usuario un número entero positivo y muestra 
# por pantalla todos los números impares desde 1 hasta ese número separados por comas.

n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

# Mejora by Continue

print("\n")
n = int(input("Introduce un número entero positivo: "))
print("Números impares desde 1 hasta", n, ": ", end="")
for i in range(1, n+1, 2):
    if i != n-1 and i != n-2:
        print(i, end=", ")
    else:
        print(i, end="")