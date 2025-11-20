# convertidor de unidades de temperatura
temperatura_celsius=float(input("ingrese la temperatura en grados Celsius:"))
temperatura_fahrenheit=(temperatura_celsius*9/5)+32
if temperatura_celsius<=-273.15:
    print("la temperatura ingresada es menor al cero absoluto, ingrese una temperatura valida")
elif temperatura_celsius>-273.15:
    print("la temperatura en grados Fahrenheit es:",temperatura_fahrenheit)
    