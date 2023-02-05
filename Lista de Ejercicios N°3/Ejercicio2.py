

##Realizar un programa que realice las siguientes funciones de string al texto.


#split: El split()método divide una cadena en una lista.
#join
#count
#find
#uppercase
#lowercase


msg = """Elija una de las siguientes opciones del menu que haran cumplir algunas funciones:
a. Split
b. Join
c. Count
d.Find
e.Uppercase
f.Lowercase
"""
print (msg)
print ("Recuerda: el texto es Lorem Ipsum ")
opcionMenu= input("Ingrese la opcion del Menu: ")

txt="Lorem Ipsum"

if (opcionMenu!="a" or opcionMenu !="b" or opcionMenu!="c" or opcionMenu!= "d" or opcionMenu!= "e" or opcionMenu!="f" ):

    if(opcionMenu=="a"):
        print(txt.split(","))
    
    elif (opcionMenu=="b"):
        print("__".join(txt.split()))
        
    elif (opcionMenu=="c"): # devuelve el número de ocurrencias de una subcadena en la cadena dada.
        Sub_string=input("Ingrese la letra o palabra que desea contar: ")
        print(txt.count(Sub_string))
    
    elif(opcionMenu=="d"):
        Sub_string=input("Ingrese la letra o palabra que desea encontrar: ")
        print(txt.find(Sub_string)) ##retorna la posición en la que se encuentre la substring
    
    elif(opcionMenu=="e"):
        print(txt.upper()) #convertir letras minúsculas en una cadena a mayúsculas
    
    elif(opcionMenu=="f"):
        print(txt.lower()) #devuelve las cadenas en minúsculas de la cadena dada
else: 
 print("Esa opcion no existe en el menu")