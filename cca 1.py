# calculo del salario con horas extras 
horas_trabajadas=int(input("ingrese la cantidad de horas trabajadas en la semana:"))
valor_hora=int(input("ingrese el valor por hora trabajada:"))   
if horas_trabajadas >40:
    horas_extras=horas_trabajadas-40
    pago_horas_extras=horas_extras*(valor_hora*1.5)
    pago_horas_normales=40*valor_hora
    salario_semanal=pago_horas_normales+pago_horas_extras
    print("el salario semanal es:",salario_semanal)
elif horas_trabajadas <=40:
    salario_semanal=horas_trabajadas*valor_hora
    print("el salario semanal es:",salario_semanal)

    //prueba
    