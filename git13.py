#descuento por cantida de compra

cantidad_productos = int(input("Cantidad de productos: "))
producto = input("Ingresa producto: ")
precio = int(input("Ingresa precio por unidad: "))
total = cantidad_productos * precio

if total >= 100:
    descuento = total * 0.10  
    total_con_descuento = total - descuento
    print(f"Producto: {producto}")
    print(f"Total sin descuento: ${total:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
if total < 100:
    print(f"Producto: {producto}")
    print(f"Total a pagar: ${total:.2f}")