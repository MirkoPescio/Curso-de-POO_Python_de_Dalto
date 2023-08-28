"""
Ejercicio 3:

Ejercicio de herencia múltiple y MRO:

Imagina que estás modelando animales en un zoológico. Crear 3 clases: 'Animal', 'Mamífero' y 'Ave'. La clase Animal debe
tener un método llamado comer(). La clase Mamífero debe tener un método llamado amamantar() y la clase Ave un método
llamado volar().

Ahora, crea una clase Murciélago que herede de Mamifero y Ave, en ese orden, y por lo tanto debe ser capaz de amamantar()
y volar(), además de comer().

Finalmente, juega con el orden de herencia de la clase Murciélago y observa cómo cambia el MRO y el comportamiento de los
métodos al usar super().
"""

# Mi solución:

class Animal:
    def __init__(self):
        pass
    def comer(self):
        print("Comer!!")

class Mamifero(Animal):
    def __init__(self):
        pass
    def amamantar(self):
        print("Amamantar")

class Ave(Animal):
    def __init__(self):
        pass
    def volar(self):
        print("Volar!")

class Murcielago(Mamifero, Ave):
    def __init__(self):
        super().__init__()


def main():
    murcielago = Murcielago()
    murcielago.comer()
    murcielago.amamantar()
    murcielago.volar()
main()

print("\n")

# Solución de Dalto:

class Animal:
    def comer(self):
        print("El animal está comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal está volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

print("Murciélago:")
murcielago.comer()
murcielago.amamantar()
murcielago.volar()
print("")

ave = Ave()

print("Ave:")
ave.comer()
ave.volar()

