#Categoría de un examen
nota=int(input("ingrese la nota del examen (0-100):"))
if nota <50 :
    print("Muy deficiente")
elif nota >=50 and nota <64:
    print("Deficiente")
elif nota >=65 and nota <74:
    print("Regular")
elif nota >=75 and nota <89:
    print("Bueno")
elif nota >=90 and nota <99:
    print("Excelente")
elif nota ==100:
    print("Perfecto")
else:
    print("Nota no válida. Por favor ingrese una nota entre 0 y 100.")