
## Menu Iterativo
msg= """Realizar un Menú Iterativo que tenga las siguientes opciones(Solo poner el número de la
pregunta):
a. Realizar un programa que dibuje un cuadrado en consola con *, usando bucles.
b. Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
c. Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad."""
 
print (msg)

opcionMenu= input("Ingrese la opcion del Menu: ")


if (opcionMenu!= "a" or opcionMenu!= "b" or opcionMenu!= "c"):
    
   if opcionMenu =="a": ##Opcion a
       filas= int(input("Ingrese la cantidad de filas: "))
       columnas= int(input("Ingrese la cantidad de columnas: "))

       for i in range (1, filas):
           for j in range (1, columnas):
                 print ("*",end="")
           print("")
   elif opcionMenu == "b": ## Opcion b
       Numero = []
       Agregar_numero= int(input("Ingrese un numero: "))
       Numero.append(Agregar_numero)
       for Agregar_numero in Numero:
           if Agregar_numero%2==0 :
               print ("El numero " , Numero , "es multiplo de 2")
           else :
               print("El numero " , Numero , "no es multiplo de 2")
   elif opcionMenu== "c" : #opcion c
       personas=[["Jorge",25],["Juan",15],["Kathy", 23],["Luis",18],["Manuel", 5]]
       personas_mayores=[] 
       
       for personas_mayores in personas:
        if personas_mayores[1]>= 18 :
            print("Las personas con mayor a 18 años son: " , personas_mayores)            
else : 
     print(" Elija la opcion correcta ")
        