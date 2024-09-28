class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

colaBanco = Cola()
colaBanco.agregar("persona12")
colaBanco.agregar("persona25")
colaBanco.agregar("persona9")
colaBanco.agregar("persona97")

print("persona atendida:", colaBanco.avanzar()) #desencola "persona12"
print("persona atendida:", colaBanco.avanzar()) #desencola "persona25"