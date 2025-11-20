# raiz cuadrada que sea positiva
numero=int(input("ingrese un numero:"))
if numero>=0:
    raiz=numero**0.5
    print("la raiz cuadrada es:",raiz)
if numero<0:
    print("el numero es negativo, no se puede calcular la raiz cuadrada")