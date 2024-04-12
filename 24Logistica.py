# Cada payaso pesa 112 g y cada muñeca 75 g. Programa que lee el número de payasos y muñecas 
# vendidos en el último pedido y calcula el peso total del paquete que será enviado.

peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))