#Multiplicidad y paridad de dos números
Num1=int(input("ingrese un número:"))
Num2=int(input("ingrese otro número:"))
if Num1 %2 ==0 and Num2 %2 ==0:
    print("ambos números son pares")
elif Num1 %2 !=0 and Num2 %2 !=0:
    print("ambos números son impares")
elif Num1 %2 ==0 and Num2 %2 !=0:
    print(f"el {Num1} número es par  y el {Num2} es impar")
elif Num1 %2 !=0 and Num2 %2 ==0:
    print(f"el {Num1} número es impar y el {Num2} es par")
if  Num1 % Num2 ==0:
    print(f"el {Num1} es múltiplo de {Num2}")
elif Num2 % Num1 ==0:
    print(f"el {Num2} es múltiplo de {Num1}")
else:
    print("los números no son múltiplos entre sí")