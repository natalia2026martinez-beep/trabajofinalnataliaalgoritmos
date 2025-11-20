#calculo de descuento basado en categoria del cliente
categoria_cliente =input("Ingrese la categoría del cliente (A, B, C): ")
if categoria_cliente == "A":
    descuento = 0.20
    print("El monto final con descuento es:")
elif categoria_cliente == "B":
    descuento = 0.10
    print("El monto final con descuento es:")
elif categoria_cliente == "C":
     descuento = 0.05
     print("No aplica descuento. El monto a pagar es:")
else:
     print("Categoría no válida. Por favor ingrese A, B o C.")
