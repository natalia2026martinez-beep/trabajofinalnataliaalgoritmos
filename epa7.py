#Determinar el trimestre de un mes
mes=int(input("ingrese un número del 1 al 12 correspondiente a un mes:"))
if mes >=1 and mes <=3:
    print("el mes",mes,"corresponde al primer trimestre del año")
elif mes >=4 and mes <=6:
    print("el mes",mes,"corresponde al segundo trimestre del año")
elif mes >=7 and mes <=9:
    print("el mes",mes,"corresponde al tercer trimestre del año")
elif mes >=10 and mes <=12:
    print("el mes",mes,"corresponde al cuarto trimestre del año")
else:
    print("número de mes no válido. Por favor ingrese un número entre 1 y 12.")