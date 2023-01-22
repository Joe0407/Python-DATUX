## Definir una función que retorne el mayor valor al ingresar 2 números


def mayor_valor(a,b):
    if a > b: 
        return a
    elif a< b:
        return b
    else :
        print (" Los dos numeros son iguales ".format(a,b))
        
## print (mayor_valor(15,15))

a = int (input("Ingrese el primer valor: "))
b = int (input("Ingrese el segundo valor: "))

Mayor = mayor_valor(a,b)
print (Mayor)

