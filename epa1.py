#Validez de una contraseña Pide una contraseña y verifica si es válida

contraseña=str(input("ingrese una contraseña de al menos 8 caracteres:"))
if len(contraseña)>=8:
    tiene_mayuscula=False
    tiene_minuscula=False
    tiene_numero=False
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula=True
        elif char.islower():
            tiene_minuscula=True
        elif char.isdigit():
            tiene_numero=True
    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        print("La contraseña es válida.")
    else:
        print("La contraseña no es válida. Debe contener al menos una mayúscula, una minúscula y un número.")