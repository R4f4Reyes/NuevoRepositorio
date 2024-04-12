# Programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 

edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")