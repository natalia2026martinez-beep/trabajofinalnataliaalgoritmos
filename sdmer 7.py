#Comparación de edades
edad1=int(input("ingrese la edad de la primera persona:"))
edad2=int(input("ingrese la edad de la segunda persona:"))
edad3=int(input("ingrese la edad de la tercera persona:"))
if edad1>edad2 and edad1>edad3:
    print("la primera persona es la mayor con:",edad1,"años")
elif edad2>edad1 and edad2>edad3:
    print("la segunda persona es la mayor con:",edad2,"años")   
elif edad3>edad1 and edad3>edad2:
    print("la tercera persona es la mayor con:",edad3,"años")
elif edad1==edad2 and edad1>edad3:
    print("la primera y segunda persona son las mayores con:",edad1,"años") 
elif edad1==edad3 and edad1>edad2:  
    print("la primera y tercera persona son las mayores con:",edad1,"años")
elif edad2==edad3 and edad2>edad1:
    print("la segunda y tercera persona son las mayores con:",edad2,"años")
elif edad1==edad2 and edad1==edad3:
    print("las tres personas tienen la misma edad de:",edad1,"años")

if edad1<edad2 and edad1<edad3:
    print("la primera persona es la menor con:",edad1,"años")
elif edad2<edad1 and edad2<edad3:
    print("la segunda persona es la menor con:",edad2,"años")   
elif edad3<edad1 and edad3<edad2:
    print("la tercera persona es la menor con:",edad3,"años")
elif edad1==edad2 and edad1<edad3:
    print("la primera y segunda persona son las menores con:",edad1,"años") 
elif edad1==edad3 and edad1<edad2:  
    print("la primera y tercera persona son las menores con:",edad1,"años")
elif edad2==edad3 and edad2<edad1:
    print("la segunda y tercera persona son las menores con:",edad2,"años")

