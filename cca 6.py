#edad para votar
edad=int(input("ingrese su edad:"))
if edad<18:
    print("no puede votar")
elif edad>=18 and edad<=70:
    print("es obligatorio votar")