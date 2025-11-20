#calculo de penalización por dias de retraso
dias_retraso=int(input("ingrese los dias de retraso en la devolucion del libro:"))
if dias_retraso<=0:
    print("no hay penalización")
elif dias_retraso>0 and dias_retraso<=5:
    penalización=dias_retraso*0.50
    print("la penalización es de:",penalización)
elif dias_retraso>5 and dias_retraso<=10:
    penalización=dias_retraso*1.00
    print("la penalización es de:",penalización)
elif dias_retraso>10:
    penalización=dias_retraso*5.00
    print("la penalización es de:",penalización)  