# Función que recibe una muestra de números en una lista 
# y devuelve otra lista con sus cuadrados.

def square(sample):
 
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square([1, 2, 3, 4, 5]))
print(square([2, 5, 6, 9, 12, 15]))
print("")
# Mejora by Continue.

def square(sample):
    return [i**2 for i in sample]

print(square([1, 2, 3, 4, 5]))
print(square([2, 5, 6, 9, 12, 15]))