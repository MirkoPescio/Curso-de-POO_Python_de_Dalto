"""
Decorador @property

Este es un decorador reservado para las clases en las cuales lo que hace es marcar los métodos como getters
Es decir en vez de llamar el método: persona1.presentacion(), lo voy a llamar como persona1.presentacion
"""

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    
dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Pepe"

nombre = dalto.nombre
print(nombre)

# Usanto la propiedad para eliminar dalto.nombre:

# del dalto.nombre
# nombre = dalto.nombre
# print(nombre)