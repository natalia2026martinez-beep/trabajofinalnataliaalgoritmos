#validez de un triangulo
lado1=int(input("ingrese el valor del primer lado:"))
lado2=int(input("ingrese el valor del segundo lado:"))  
lado3=int(input("ingrese el valor del tercer lado:"))
if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
    print("los lados forman un triangulo")  
elif lado1+lado2<=lado3 or lado1+lado3<=lado2 or lado2+lado3<=lado1:
    print("los lados no forman un triangulo")