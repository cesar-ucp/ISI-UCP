class Pila:
    def __init__(self): #método constructor
         self.items = [] #crear una pila

        
    def estaVacia(self):
        '''
        Regresa un valor booleano 
        para determinar si la 
        pila está vacia
        '''
        return self.items == []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        if self.estaVacia():
            print("No hay elementos a extraer, la pila esta vacia")
        else:
            return self.items.pop()

    def inspeccionar(self):
        try:
            return self.items[len(self.items)-1]
        except IndexError:
            print("No hay elementos a inspeccionar")

    def tamano(self):
        return len(self.items)
     
pilaLibros = Pila() #se crea el objeto pilaLibros de la clase Pila

pilaSitios = Pila() #objeto pilaSitios de la clase Pila

pilaLibros.incluir("libro1")
pilaLibros.incluir("libro2")
pilaLibros.incluir("libro3")

pilaSitios.incluir("www.ucp.edu.ar")
pilaSitios.incluir("www.netflix.com")
pilaSitios.incluir("github.com")

print(pilaLibros.tamano())

