class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola! Estoy hablando un poco\n")
        
# De la siguiente forma (súper sencilla) adquirimos todas las propiedades de la clase Persona en la clase Empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

roberto = Empleado("Roberto", 43, "argentino", "Operario de depósito", 130000)

print(roberto.nombre)
print(roberto.edad)
print(roberto.nacionalidad + "\n")

roberto.hablar()

print(roberto.trabajo)
print(roberto.salario)
