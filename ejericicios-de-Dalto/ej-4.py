"""
CREAR UN JUEGO DE FUSIÓN

El juego consiste en crear personajes. Un juego en el que los personajes se puedan fusionar para formar personajes más
poderosos que tengan más poder...

Para ello debemos cambiar el comportamiento del operador '+' para que cuando los personajes se fusionen, salga un nuevo
personaje con habilidades mejoradas.

Una posible fórmula es: el promedio de las habilidades de ambos, al cuadrado!
"""

# Mi solución

class Personaje:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
        
    def __str__(self):
        return f'Personaje(nombre={self.nombre}, poder={self.poder})'
    
    def __repr__(self):
        return f'Personaje("{self.nombre}", {self.poder})'
        
    def __add__(self, otro):
        nuevo_nombre = self.nombre[:-1] + otro.nombre[::-1][0]
        nuevo_poder = ((self.poder + otro.poder)/2)**2
        return (nuevo_nombre, nuevo_poder)
    
def main():
    personaje1 = Personaje("Vegeta", 28000000)
    personaje2 = Personaje("Kakarotto", 30000000)
    print(personaje1)
    print(personaje2)
    fusion = personaje1 + personaje2
    print(fusion)
main()

print("\n")

# Solución de Dalto:

class Character:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**2
        return (nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
goku = Character("Gokú", 100, 100)
print(goku)
vegeta = Character("Vegeta", 99, 99)
print(vegeta)
print("")

gogeta = goku + vegeta
print(gogeta)
