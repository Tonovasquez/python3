#Alexander
#realizar el promedio de N notas utilizando el for
print("bienbenidos al programa".center(50,"*"))
N = 0
suma = 0
print("ingrese notar que usted requiera pulse 1 para detener:.")
notas = int(input("ingrese la cantidad de notas:."))
for i in range (notas):
    N = int(input("ingrese nota:."))
   suma = suma + N
promedio = suma / notas
print("el promedio es:.{}".format(promedio))
