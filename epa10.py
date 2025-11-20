#Determinar la fase de la vida
edad=int(input("ingrese su edad:"))
if edad >=0 and edad <=12:
    print("usted es un niño")
elif edad >=13 and edad <=17:
    print("usted es un adolescente")
elif edad >=18 and edad <=59:
    print("usted es un adulto")
elif edad >=60:
    print("usted es un adulto mayor")
else:
    print("edad no válida. Por favor ingrese una edad correcta.")