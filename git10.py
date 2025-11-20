# año bisiesto
num=int(input("año:"))
if num %4==0 and num % 100 !=0 or num % 400==0:
    print(f"El año es Disiesto: {num}")
if num %4!=0 or num % 100==0 and num % 400!=0:
    print(f"El año no es Disiesto: {num}")
    
    