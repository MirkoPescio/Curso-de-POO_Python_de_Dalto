"""
1er principio => SRP

Una clase solamente tiene que tener UNA y SÓLO UNA razón para cambiar, es decir, que una clase tiene que tener una
única responsabilidad o tarea
"""

""" class Auto():
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
        
    def mover(self, distancia):
        if (self.combustible >= (distancia/2)):
            self.posicion += distancia
            self.combustible -= (distancia/2)
        else:
            print("No hay suficiente combustible")
            
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible """
        
# El problema con el código anterior, es que no respeta el primer principio de SOLID

# ¿Cómo podemos optimizarlo? Dividiendo la clase

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if (self.tanque.obtener_combustible() >= (distancia/2)):
            self.posicion += distancia
            self.tanque.usar_combustible(distancia/2)
            print("Moviste el auto exitosamente")
        else:
            print("No hay suficiente combustible")
            
    def obtener_posicion(self):
        return self.posicion

def main():
    tanque = TanqueDeCombustible()
    auto1 = Auto(tanque)
    print(auto1)
    print("\n")
    print(auto1.obtener_posicion())
    print(auto1.mover(10))
    print(auto1.obtener_posicion())
    print(auto1.mover(20))
    print(auto1.obtener_posicion())
    print(auto1.mover(60))
    print(auto1.obtener_posicion())
    print(auto1.mover(100))
    print(auto1.obtener_posicion())
    print(auto1.mover(100))
    print(auto1.obtener_posicion())
main()

