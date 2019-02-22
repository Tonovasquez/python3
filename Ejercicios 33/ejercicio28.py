#Elavore un programa que perimita ingresar le precio y la cantidad de un articulo a
#comprar. Calcular el tota a pagar. (Considerar el IVA 9%)
iva = 0.09
precio = float(input("ingrese el precio:."))
cantidad = int(input("ingrese cuanto va a llevar:."))
total = precio * cantidad
iva_a_pagar = total * iva
total_a_pagar = total + iva_a_pagar
print("el total  es:.{}".format(total))
print("el iva a pagar es:.{}".format(iva_a_pagar))
print("el total a pagar es:.{}".format(total_a_pagar))
