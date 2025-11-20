# verificacion de usuario y la contraseña
usuario=str(input("ingrese su nombre de usuario:"))
contraseña=str(input("ingrese su contraseña:"))
if usuario=="natalia" and contraseña=="12345":
    print("acceso concedido")
elif usuario!="natalia" or contraseña!="12345":
    print("acceso denegado")
    