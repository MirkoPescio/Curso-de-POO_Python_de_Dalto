"""
Polimorfismo:

Basicamente se trata de hacer, que cuando le demos un método a un objeto, este se comporte de una forma diferente al
entender que sus propiedades son diferentes

MISMO MENSAJE <==> RESULTADO DIFERENTE
"""

# Ejemplo básico:

class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())
print("\n")

# Mismo Polimorfismo, pero aplicado de otra manera:

def hacer_sonido(animal):
    return animal.sonido()

print(hacer_sonido(gato))
print(hacer_sonido(perro))

"""
Otra explicación de Dalto:

Polimorfismo de sobrecarga de métodos:

Crear un mismo método, pero depende de la cantidad y tipos de parámetros que le pase, va ejecutar una serie de tareas
determinadas.

Un ejemplo sería el siguiente
"""

class Persona():
    def presentacion(self):
        pass
    def presentacion(self, nombre):
        pass
    def presentacion(self, nombre, edad):
        pass
    def presentacion(self, nombre, edad, ID):
        pass

