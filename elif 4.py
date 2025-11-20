#categoria de velocidad 
velocidad=int(input("ingrese la velocidad del vehiculo en km/h:"))
if velocidad >=100:
    print("velocidad alta")
elif velocidad >=60 and velocidad <100:
    print("velocidad normal")
elif velocidad <60:
    print("velocidad baja")