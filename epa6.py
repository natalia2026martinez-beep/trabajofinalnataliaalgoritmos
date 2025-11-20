#Descuento en función de la hora de compra
hora_compra=int(input("ingrese la hora de compra (0-24):"))
monto_compra=int(input("Monto de la compra:"))
if hora_compra >=0 and hora_compra <12:
    descuento=monto_compra*0.10
    total_pago=monto_compra - descuento
    print("el total a pagar con descuento es de:",total_pago)
elif hora_compra >=12 and hora_compra <=18:
    descuento=monto_compra*0.20
    total_pago=monto_compra - descuento
    print("el total a pagar con descuento es de:",total_pago)
elif hora_compra >18 and hora_compra <=24:
    print("no aplica descuento. El monto a pagar es de:",monto_compra)
else:
    print("hora no válida. Por favor ingrese una hora entre 0 y 24.")
