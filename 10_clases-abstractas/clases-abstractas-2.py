from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, genero, actividad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy trabajando de: {self.actividad}")
    

def main():
    mirko_estudiante = Estudiante("Mirko", 24, "Masculino", "Programación")
    mirko_trabajador = Trabajador("Mirko", 24, "Masculino", "Operario de depósito")
    mirko_estudiante.hacer_actividad()
    mirko_trabajador.hacer_actividad()
    print("\n")
    pedrito_estudiante = Estudiante("Pedrito", 25, "No Binario", "Filosofía")
    pedrito_estudiante.presentarse()
    pedrito_estudiante.hacer_actividad()
main()
