# Función que calcula el total de una factura tras aplicarle el IVA. 
# La función recibie la cantidad sin IVA y el porcentaje de IVA a aplicar,
# y devuelve el total de la factura. Si se invoca la función sin pasarle 
# el porcentaje de IVA, deberá aplicar un 21%.

def invoice(amount, vat=21):
   
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))

# Mejora. By Continue.

def invoice(amount, vat=21):
    total = amount + amount*vat/100
    return f"Total invoice: {total} (including {vat}% VAT)"

print(invoice(1000,10))
print(invoice(1000))