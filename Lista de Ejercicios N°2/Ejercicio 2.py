## Mini programa de una Biblioteca

Sistema = {
    'Nombre de la Biblioteca' : 'Biblioteca Phoenix',
    'Libros_Autores' : [['Odisea','Homero'],['Metamorfosis','Kafka'],
                        ["Caballero Carmelo","A. Valdelomar"],['Romeo y Julieta','W. Shakespeare']],
    'Categorias': ['Romance', 'Aventura', 'Ficcion', 'Terror'],
    'Estado' : ['Prestado', 'No prestado','En biblioteca'],
    'Libros_Estado': [('Odisea','No prestado'),('Romeo y Julieta', 'Prestado')],
    'Usuario' : {
        "1000": {
            'Nombre' : 'Jose',
            'Apellido' : 'Ariarte',
            'Libro' : ['Odisea','Homero'],
            'Estado': ['No prestado']
        },
         "1001": {
            'Nombre' : 'Maria',
            'Apellido' : 'Valdivia',
            'Libro' : ['Romero y Julieta','W. Shakespeare'],
            'Estado': ['Prestado']
        }
        
    }

}

msg= """La biblioteca deberá tener las siguientes operaciones:
 a. Obtener la lista de categorías de libros.
 b. Obtener nombres de los libros y autores.
 c. poder cambiar el estado de un libro a prestado
 d. Lista de usuarios de la biblioteca."""

print(msg)

Menu = input('Ingrese la opcion que desea ')

if (Menu!= "a" or Menu!= "b" or Menu!= "c" or Menu != "d"):  
    if Menu == 'a' :
        print ("La lista de categorias son: " , Sistema['Categorias'])
    
    
    print ("")
else: 
    print ("La opcion no esta en el menu")
    
