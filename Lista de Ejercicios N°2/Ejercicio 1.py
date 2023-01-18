
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
       Numero = [3,15,20,24,60,35,36]
       if Numero % 2 == 0:
            print ("El numero", Numero, "si es multiplo de 2")
       else: 
           print (" El numero", Numero , "no es multipo de 2")
    