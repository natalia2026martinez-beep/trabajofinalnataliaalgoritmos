#calculadora de impuestos 
ingreso_anual=int(input("ingrese su ingreso anual en USD:"))
if ingreso_anual <=11000:
    print("no paga impuestos")
elif ingreso_anual >11000 and ingreso_anual <=50000:
    impuesto=ingreso_anual*0.15
    print("el impuesto a pagar es de:",impuesto,"USD")