#rango de puntaje
puntaje_examen=int(input("ingrese su puntaje del examen:"))
if puntaje_examen>=90 and puntaje_examen<=100:
    print("A")  
elif puntaje_examen>=75 and puntaje_examen<90:
    print("B")  
elif puntaje_examen>=50 and puntaje_examen<75:
    print("C")
elif puntaje_examen>=0 and puntaje_examen<50:
    print("D")
elif puntaje_examen<0 or puntaje_examen>100:
    print("F")
