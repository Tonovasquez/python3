# antony
#necesitan crear un programa de una una a dos opciones
#1.convertir dolares a quetzales
#2.convertir de quetzales a dolares
#si el usuario ingresa a una opcion invalida que es incorrectara
print("Bienbenido al programa".center(50,"*"))

D = 7.80
print("ingrese 1 para convertir D a Q o ingrese 2 para convertir Q a D:.")
convertir = int("ingrese 1 o 2 para convertir:."
 if convertir == 1:
  Q = float(input("ingrese la cantidad que desea convertir:.")
  resultado = Q * D
  print("La conversion es Q:. {}".format( Q * D ))
 elif convertir == 2:
  Q = float(input("Ingrese la cantidad:.")
  Resultado = Q / D
  print("La conversion es D:. {}".format( Q / D ))

 else:
    print("dato incorrecto")
