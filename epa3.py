#Asignación de tipo de sangre

tipo_sangre=input("ingrese su tipo de sangre (A, B, AB, O):")
if tipo_sangre=="A":
    print("Puede donar a: A, AB")
    print("Puede recibir de: A, O")
elif tipo_sangre=="B":
    print("Puede donar a: B, AB")
    print("Puede recibir de: B, O")
elif tipo_sangre=="AB":
    print("Puede donar a: AB")
    print("Puede recibir de: A, B, AB, O")
elif tipo_sangre=="O":
    print("Puede donar a: A, B, AB, O")
    print("Puede recibir de: O")
else:
    print("Tipo de sangre inválido.")