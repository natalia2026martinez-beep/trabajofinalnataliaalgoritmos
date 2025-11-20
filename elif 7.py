#numero mas cercano a 100
num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
diferencia1=(100 - num1)
diferencia2=(100 - num2) 
if diferencia1<diferencia2:
    print("el numero mas cercano a 100 es:",num1)       
elif diferencia2<diferencia1:
    print("el numero mas cercano a 100 es:",num2)
elif diferencia1==diferencia2:
    print("ambos numeros son igualmente cercanos a 100")