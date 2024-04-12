# Función que recibe un número entero positivo y devuelva su factorial.

def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factorial(4))
print(factorial(20))

# Versión mejorada. By Continue.

def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

numero = int(input("Ingrese un número entero positivo: "))
print(factorial(numero))