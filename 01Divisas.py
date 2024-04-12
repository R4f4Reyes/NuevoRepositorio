# Diccionario de divisas

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} # Aquí se guardan los datos del diccionario
moneda = input ("Introduce una divisa: ")
print (monedas.get(moneda.title(),"La divisa no está."))


# Diccionario de divisas actualizado con más opciones. From Continue.
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥', 'Libra':'£',
            'Franco Suizo':'CHF', 'Dólar Canadiense':'CAD', 'Peso Mexicano':'MXN'}

while True: # Inicia ciclo de repetición
    moneda = input("Introduce una divisa: ")
    print(monedas.get(moneda.title(), "La divisa no está."))
    otra_consulta = input("¿Deseas hacer otra consulta? (s/n): ")
    if otra_consulta.lower() != 's': # Si la respuesta es diferente a s (si), el programa termina
        break