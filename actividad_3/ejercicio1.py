#Alexander
#Solicitar al usuario que seleccione una opcion y elevar el primer numero al segundo numero:
#1.soliciitar 3 numeros y elevar el primero con el segundo y el resultado elevarlo al 3.
elevacion = 0

print("bienbenido al programa".center(50,"*"))
opcion = input("1.elevar el primero con el segundo 2.solicitar tres numeros y elevar el primero con el segundo y el resultado elevarlo a la 3:.")

if opcion == "1":
    valor1 = int(input("ingrese valor1:."))
    valor2 = int(input("ingrese valor2.."))
    elevacion = valor1 ** valor2
    print("la elevacion es:.{}".format(elevacion))

elif opcion == "2":
    valor1 = int(input("ingrese valor1:."))
    valor2 = int(input("ingrese valor2.."))
    valor3 = int(input("ingrese valor3.."))
    elevacion = (valor1 ** valor2) ** valor3
    print("la elevacion es:.{}".format(elevacion))
else:
    print("opcion incorrecta")









