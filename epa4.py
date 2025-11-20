#Día de la semana y si es fin de semana
#Pide un día de la semana y determina si es fin de semana o día laboral.
dia_semana=input("ingrese un día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo):").lower()
if dia_semana =="sábado" or dia_semana =="domingo":
    print(dia_semana, "es fin de semana.")  
elif dia_semana =="lunes" or dia_semana == "martes"or dia_semana =="miércoles"or dia_semana == "jueves"or dia_semana =="viernes":
    print(dia_semana, "es un día laboral.")
else:
    print("Entrada no válida. Por favor ingrese un día de la semana correcto.")