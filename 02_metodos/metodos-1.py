# Para resumir => un método es una función
# Los cuales vamos a definir en una clase

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def llamar(self):
        print(f"Estás haciendo una llamada desde un {self.modelo}")
    def cortar(self):
        print("Cortaste la llamada")
        
celular_1 = Celular("Samsung", "A10", "14MP")
celular_2 = Celular("Motorola", "Moto E6 Plus", "14MP")
celular_3 = Celular("Apple", "Iphone X", "32MP")


celular_1.llamar()
celular_1.cortar()
print("\n")

celular_2.llamar()
celular_2.cortar()
print("\n")

celular_3.llamar()
celular_3.cortar()
print("\n")

