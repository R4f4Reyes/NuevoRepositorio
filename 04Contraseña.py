# Almacena "contraseña" y evalua si la contraseña ingresada por el usuario es verdadera o no
# No toma importancia en mayúsculas o minúsculas

key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower(): # Esto restringe la importancia de mayúsculas y minúsculas
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

# Toma importancia en mayúsculas y minúsculas

key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password: # Aquí ya se vuelve mas estricto con los caracteres ingresados
    print("La contraseña coincide")
else:
    print("La contraseña no coincide. Asegúrate de escribir la contraseña exactamente como se te proporcionó, incluyendo mayúsculas y minúsculas.")