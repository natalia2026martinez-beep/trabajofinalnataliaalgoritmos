# aprobado o reprobado con mensión especial
nota=int (input("ingrese la nota del estudiante:"))
if nota <60:
  print("el estudiante está reprobado")
if nota >=60 and nota <90:  
  print("el estudiante está aprobado")
if nota >=90:
  print("el estudiante está aprobado especial")