# determinar el trimestre
mes=int(input("ingrese el numero del mes (1-12):"))
if mes >=1 and mes <=3:
    print("el mes corresponde al primer trimestre")     
elif mes >=4 and mes <=6:
    print("el mes corresponde al segundo trimestre")
elif mes >=7 and mes <=9:
    print("el mes corresponde al tercer trimestre")
elif mes >=10 and mes <=12:
    print("el mes corresponde al cuarto trimestre")