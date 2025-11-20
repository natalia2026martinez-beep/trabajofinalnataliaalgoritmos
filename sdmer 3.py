#clasififcación de temperatura
temperatura=int(input("escribe los grados centigrados:"))
if temperatura <=0:
    print("muy frio")
elif temperatura <=10:
    print ("frio")
elif temperatura <=30:
    print("tibio")
elif temperatura <=35:
    print("caliente")
else:
    temperatura >=40
    print("muy caliente")