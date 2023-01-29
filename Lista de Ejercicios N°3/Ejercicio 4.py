## definiendo la clase catalogo y producto

##Clase producto

class Producto :
    
    ##Init 
    
    def __init__(self, Codigo , Descripcion, Precio , Proveedor):
        self.Codigo = Codigo,
        self.Descripcion = Descripcion,
        self.Precio = Precio,
        self.Proveedor = Proveedor
        
        print ('Se ha agregado el siguiente Producto: {} '.format(self.Descripcion))
        
    def __str__(self) -> str:
        return """ 
         codigo: {} 
         Descripcion: {} """.format(self.Codigo, self.Descripcion)
    

class Catalogo: 
    
    producto = []
    
    def __init__(self, producto = []) :
        self.producto = producto
    
    def agregar (self , p):
        self.producto.append(p)
    
    def mostrar (self):
        for p in self.producto:
            print (p)
        
        
p = Producto("P0001", "Lapiceros", 5.00 , "Caleb")
c= Catalogo([p])
c.mostrar()

##Agregar datos

c.agregar(Producto("P0002" , "Cuadernos" , 3.50 , "Loro"))
c.mostrar()
