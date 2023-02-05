from Ejercicio5 import funRec_SumaNumeros
from Ejercicio5 import dividir

try:
    numero= int(input("Ingrese el numero: "))
    funRec_SumaNumeros(numero)
    ######
    
    a=int(input("Ingresa el primer valor: "))
    b=int(input("Ingresa el segundo valor: "))
    dividir(a,b)
except:
    print ("No existe funcion")
else:
     funRec_SumaNumeros(numero)
     dividir(a,b)