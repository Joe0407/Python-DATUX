##Creando funciones para el modulo 

##Una función recursiva de suma de los n primeros números



def funRec_SumaNumeros(numero):
    
    if numero == 1 :
        print("La suma del primer numero es: ",numero)
    else:
        
        Suma_Numeros = (numero*(numero + 1))/2
        
        print ("La suma de los {} numeros es: {}".format(numero,Suma_Numeros))
        funRec_SumaNumeros(numero-1)



numero= int(input("Ingrese el numero: "))
funRec_SumaNumeros(numero)





#Una función que me permita dividir 2 números.

def dividir(a,b):
    if(b==0):
        print("Solucion indefinida. No se puede dividir entre 0")
    else: 
        Resultado= a/b
        print("La division entre los numeros {} y {} es: {}".format(a,b,Resultado))
        
a=int(input("Ingresa el primer valor: "))
b=int(input("Ingresa el segundo valor: "))
dividir(a,b)