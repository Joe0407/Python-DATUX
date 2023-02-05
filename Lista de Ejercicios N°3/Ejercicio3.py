 ##Realizar una función que pase un entero por valor y lo multiplique por 2 y otra función
 
a = int(input("Ingrese el valor: "))
 
def doble (a):
    return a*2


def triple (b):
    return b*3

resultado= triple(doble(a))

print (resultado)