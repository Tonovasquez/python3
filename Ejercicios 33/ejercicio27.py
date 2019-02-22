#Elavore un programa que calcule la edad exacta de una persona
print("bienvenidos al programa".center(50,"*"))
año_actual = 2019
año = int(input("ingrese año de nacimiento:."))
mes = int(input("ingrese mes de nacimiento:."))
dia = int(input("ingrese dia de nacimiento:."))

años_que_tiene = año_actual - año
print("su año actual es:.{}".format(años_que_tiene))
if años_que_tiene >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
