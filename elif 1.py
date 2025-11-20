#clasificacion de una calificación
calificación=int(input("pide una calificación:"))
if calificación >=90 and calificación <=100:
    print("excelente")      
elif calificación >=80 and calificación <90:
    print("Buena")      
elif calificación >=60 and calificación <80:
    print("regular")

elif calificación <=60 and calificación >=0:
    print("mala")
