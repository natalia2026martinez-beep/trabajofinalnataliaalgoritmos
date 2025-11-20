#Temperatura de ebullición y congelación
temperatura=float(input("ingrese la temperatura en grados centígrados:"))
if temperatura <=0:
    print("el agua está congelada")
elif temperatura >=100:
    print("el agua está hirviendo")
else:
    print("el agua está tibia")     