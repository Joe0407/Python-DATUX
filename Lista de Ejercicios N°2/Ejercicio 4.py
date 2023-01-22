import sys

print (" Todos los argumentos pasados desde la linea de comando: " ,sys.argv)

## definiendo una funcion 

def Suma(a,b):
    return a + b

a = int(input("Ingrese un valor: " , sys.argv[0]))
b = int(input("Ingrese otro valor: " , sys.argv[1]))

resultado = Suma(a+b)

Suma(a,b)
