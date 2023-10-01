"""
Una clase abstracta es una clase que no podemos instanciar, sino que es como una especie de plantilla para que podamos
crear clases a partir de esa plantilla
"""

from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    @abstractclassmethod
    def trabajar(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
        

def main():
    Mirko = Persona("Mirko", 24, "Masculino", "Operario")
main()

"""
De esta forma vemos que no es posible crear objetos a partir de una clase abstracta
"""

