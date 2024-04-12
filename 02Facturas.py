# Programa de gestión de facturas pendientes de cobro
# No olvidar poner los if en la misma columna porque luego muestra error
facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
            clave = input('Introduce el número de la factura: ')
            coste = float(input('Introduce el coste de la factura: '))
            facturas[clave] = coste
            pendiente += coste
    if more == 'P' :
            clave = input('Introduce el número de la factura a pagar: ')
            coste = facturas.pop(clave, 0)
            cobrado += coste
            pendiente -= coste
    print('Recaudado: ',cobrado)
    print('Pendiente de cobro: ',pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')

    # Con Continue, se añadio un apartado para introducir la cantidad a pagar

facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
            clave = input('Introduce el número de la factura: ')
            coste = float(input('Introduce el coste de la factura: '))
            facturas[clave] = coste
            pendiente += coste
    if more == 'P' :
            clave = input('Introduce el número de la factura a pagar: ')
            coste = facturas[clave]
            pago = float(input('Introduce la cantidad con la que se va a pagar: '))
            if pago < coste:
                print('La cantidad introducida no es suficiente para pagar la factura.')
            else:
                cobrado += coste
                pendiente -= coste
                cambio = pago - coste
                if cambio > 0:
                    print('Cambio a devolver: ', cambio)
                facturas.pop(clave)
    print('Recaudado: ',cobrado)
    print('Pendiente de cobro: ',pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')