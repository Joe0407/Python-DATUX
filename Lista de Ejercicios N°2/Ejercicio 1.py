
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

## Realizando el cuadrado Opcion a

filas= int(input("Ingrese la cantidad de filas: "))
columnas= int(input("Ingrese la cantidad de columnas: "))

for i in range (1, filas):
    for j in range (1, columnas):
        print ("*",end="")
    print("")

## Opcion b