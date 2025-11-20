# calificacion de 5 asignaturas
calificacion1=float(input("ingrese la primera calificacion Tarea:"))
calificacion2=float(input("ingrese la segunda calificacion Taller:"))
calificacion3=float(input("ingrese la tercera calificación Examen #1:"))
calificacion4=float(input("ingrese la cuarta calificacion Examen #2:"))
calificacion5=float(input("ingrese la quinta calificacion Examen #3:"))
promedio=(calificacion1+calificacion2+calificacion3+calificacion4+calificacion5)/5
if promedio<=3.5:
    print("Reprobado con un promedio de:",promedio)
elif promedio>3.5 and promedio <4.5:
    print("aprobado con un promedio de:",promedio)
elif promedio ==5.0:
    print("aprobado con promedio alto:",promedio)

