#Alexander
#Solisitar al usuario que escoja una de las siguientes opcciones:
#1.sumar dos numeros
#2.restar tres numeros
#3.multiplicar cuatro numeros
#4.dividir dos numeros
#y si el usuario ingresa una opcion invalida hacercela saber.
print("Bienbenidos al programa".center(50,"*"))
menu = '''Menu
        1.Suma
        2.Resta
        3.multiplicacion
        4.Division
        5.Salir
        '''
print (menu)
opcione = input("ingrese menu:.")
while opcion!= 5:
    if opcion == 1:
        n1 = float(input("ingrese valor1"))
        n2 = float(input("ingrese valor2"))
        suma = n1 + n2
        print("La suma es \n {}",format(suma))
    elif opcion == 2:
        n1 = float(input("ingrese valor1"))
        n2 = float(input("ingrese valor2"))
        n3 = float(input("ingrese valor3"))
        resta = n1 - n2 - n3
        print("La resta es:. {}".format(resta))
    elif opcion == 3:
        n1 = float(input("ingrese valor1"))
        n2 = float(input("ingrese valor2"))
        n3 = float(input("ingrese valor3"))
        n4 = float(input("ingrese valor4"))
        multiplicacion = n1 * n2 * n3 * n4
        print("La multiplicacion es:. {}".format(multiplicacion))
    elif opcion == 3:
        n1 = float(input("ingrese valor1"))
        n2 = float(input("ingrese valor2"))
        division = n1 / n2
        print("La division es:. {}".format(division))
    else:
        print("opcion no valida")
    print (menu)
    opcion = input("ingrese menu:.")
print ("FIN")
