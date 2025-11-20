#nota de dos parciales y examen final 
parcial1=int(input("ingrese la nota del primer parcial:"))
parcial2=int(input("ingrese la nota del segundo parcial:"))       
examenfinal=int(input("ingrese la nota del examen final:"))
promedioparciales=(parcial1+parcial2)/2
if promedioparciales >=70 and examenfinal >=60:
    print("el estudiante está aprobado")
elif promedioparciales <70 or examenfinal <60:
    print("el estudiante está reprobado")
