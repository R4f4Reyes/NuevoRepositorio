# Programa que pide al usuario su peso (en kg) y estatura (en metros), 
# calcula el índice de masa corporal y lo almacene en una variable, y 
# muestra por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el 
# índice de masa corporal calculado redondeado con dos decimales.

peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))