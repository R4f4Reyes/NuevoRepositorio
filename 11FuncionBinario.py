# Función que convierte un número decimal en binario 
# y otra que convierte un número binario en decimal.

print("")
def to_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))
print("")

# Mejora by Continue

def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

# Solicitar al usuario el número decimal a convertir
decimal_number = int(input("Ingrese un número decimal para convertir a binario: "))
print(f"El número binario correspondiente es: {to_binary(decimal_number)}")

# Solicitar al usuario el número binario a convertir
binary_number = input("Ingrese un número binario para convertir a decimal: ")
print(f"El número decimal correspondiente es: {to_decimal(binary_number)}")