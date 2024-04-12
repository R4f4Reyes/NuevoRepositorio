# Evalúa si el usuario debe pagar impuestos o no
# Si es mayor de 16 debe tributar, de lo contrario no

age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age > 16 and income >= 1000: # Aquí se evalúa la condición para tributar
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")