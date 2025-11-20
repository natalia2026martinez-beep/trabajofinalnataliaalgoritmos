#Precio con IVA
precio=int(input("ingrese el precio del producto:"))
tipo_producto=input("ingrese el tipo de producto (esencial/no esencial): ")
if tipo_producto=="esencial":
    iva=0.19
    precio_final=precio+(precio*iva)
    print("el precio final con IVA es:",precio_final)
elif tipo_producto=="no esencial":
    iva=0.04
    precio_final=precio+(precio*iva)
    print("el precio final con IVA es:",precio_final)
else:
    print("tipo de producto no válido. Por favor ingrese 'esencial' o 'no esencial'.")