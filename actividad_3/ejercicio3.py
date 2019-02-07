#Alexander
#realizar el promedio de 5 notas utilizando el siclo for
print("Bienvenidos al programa".center(50,"*"))
suma = 0
for i in range (5):
    N = int(input("ingrese N:."))
    suma = suma + N
    promedio = suma / 5
print("el prmedio es:.{}".format(promedio))
