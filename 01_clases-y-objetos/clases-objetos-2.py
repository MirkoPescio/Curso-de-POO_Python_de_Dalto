# Para este ejemplo vemos una clase con atributos a asignar (atributos no predefinidos para todos los objetos a crear)
# También conocido como constructor

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
celular_1 = Celular("Samsung", "A10", "14MP")
celular_2 = Celular("Motorola", "Moto E6 Plus", "14MP")
celular_3 = Celular("Apple", "Iphone X", "32MP")

print(celular_1.marca)
print(celular_1.modelo)
print(celular_1.camara)
print("\n")

print(celular_2.marca)
print(celular_2.modelo)
print(celular_2.camara)
print("\n")

print(celular_3.marca)
print(celular_3.modelo)
print(celular_3.camara)
print("\n")

