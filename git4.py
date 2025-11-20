#calculadora basica 
numero1=int(input("ingrese el primer numero:"))
numero2=int(input("ingrese el segundo numero:"))
operación=input("ingrese la operación a realizar (+,-,*,/):")
if operación=="+":
    resultado=numero1+numero2
    print("el resultado de la suma es:",resultado)
if operación=="-":
    resultado=numero1-numero2
    print("el resultado de la resta es:",resultado)
if operación=="*":
    resultado=numero1*numero2
    print("el resultado de la multiplicación es:",resultado)
if operación=="/":
    resultado=numero1/numero2
    print("el resultado de la división es:",resultado)