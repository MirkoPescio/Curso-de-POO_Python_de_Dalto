"""
Ejercicio 2:

Ejercicio de herencia y uso de super()

Crear un sistema para una escuela. En este sistema, vamos a tener 2 clases principales: Persona y Estudiante.
La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona. La
clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el
grado del estudiante.

Deberás utilizar super() en el método de inicialización (init) para reutilizar el código de la clase padre (Persona).
Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que
todo funciona correctamente.
"""

# Mi solución:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def grado_estudiante(self):
        print(f"{self.nombre} está en {self.grado}° grado")
        
def ingreso_de_estudiantes():
    lista_estudiantes = []
    ingreso = ""
    while (ingreso.lower() != "no"):
        nombre = input("Ingrese el nombre de un/a estudiante: ")
        edad = int(input("Ingrese su edad: "))
        while (edad <= 2 or edad >= 13):
            edad = int(input("Reingrese la edad del estudiante: "))
        grado = int(input("Ingrese el grado del estudiante (1-9): "))
        while (grado < 1 or grado > 9):
            grado = int(input("Reingrese el grado del estudiante (1-9): "))
        tupla_estudiante = (nombre, edad, grado)
        lista_estudiantes.append(tupla_estudiante)
        ingreso = input("¿Quiere seguir ingresando datos? (si/no): ")
    return lista_estudiantes
        
def main():
    lista_de_estudiantes = ingreso_de_estudiantes()
    for tupla in lista_de_estudiantes:
        estudiante = Estudiante(tupla[0], tupla[1], tupla[2])
        print(f"Nombre: {estudiante.nombre}")
        print(f"Edad: {estudiante.edad}")
        print(f"Grado: {estudiante.grado}")
        estudiante.grado_estudiante()
main()
print("\n")

# Solución de Dalto:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) # Si usamos super(), no pasamos el parámetro self
        self.grado = grado
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

estudiante = Estudiante("Juan", "14", "10mo")
estudiante.mostrar_datos()
estudiante.mostrar_grado()
