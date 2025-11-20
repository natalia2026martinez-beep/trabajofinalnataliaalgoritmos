#Edad mínima para alquilar un auto
edad=int(input("ingrese su edad:"))
costo_alquiler=7823
if edad <21:
    print("no puede alquilar un auto")
elif edad >=21 and edad <25:
    recaudo=costo_alquiler*0.15
    total_alquiler=costo_alquiler+recaudo
    print("puede alquilar un auto con un costo de :",total_alquiler)
elif edad >=25:
    print("puede alquilar un auto con un costo de :",costo_alquiler)
