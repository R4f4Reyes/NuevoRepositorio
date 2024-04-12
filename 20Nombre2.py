# Programa que pregunta el nombre completo del usuario en la consola 
#y después muestra por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
#El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. 

print ("\n")
name = input("¿Cómo te llamas? ")
print(name.lower())
print(name.upper())
print(name.title())