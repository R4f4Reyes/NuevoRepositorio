#  Programa que pregunta el nombre del usuario en la consola y 
# un número entero e imprime por pantalla en líneas distintas el 
# nombre del usuario tantas veces como el número introducido.

nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))