#Calcular el promedio de 3 notas. Si el promedio mayor que 9.5 mostrar aprobado,
#caso contrario desaprobado. Pero si la nota es mayor que 16 rodondear su
#promedio final a 20.
n1 = float(input("ingrese nota:."))
n2 = float(input("ingrese nota:."))
n3 = float(input("ingrese nota:."))
promedio = int(n1 +n2 +n3) / int(3)
print("su promedio es:.{}".format(promedio))
if promedio < 9.5 :
    print("reprobado")
elif promedio >= 9.5 :
    print("aprobado")
elif promedio > 16 and promedio < 20:
    print("promedio final")
