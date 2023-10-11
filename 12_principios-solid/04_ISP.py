"""
Principio ISP => principio de segregación de la interfaz

Este principio nos indica que ningún cliente tiene que ser forzado a depender de interfaces que no utilice.
Es decir, tenemos que eliminar las dependencias que no vamos a utilizar.
"""

from abc import ABC, abstractmethod


""" 
class Trabajador(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def trabajar(self):
        pass
    
    def dormir(self):
        pass
    
class Humano(Trabajador):
    
    def comer(self):
        print("Comiendo")
        
    def trabajar(self):
        print("Trabajando/laburando")
        
    def dormir(self):
        print("Durmiendo")

# ACLARACION: con 'INTERFAZ' nos referimos a las clases abstractas

class Robot(Trabajador):
    
    def comer(self):
        pass
    
    def trabajar(self):
        print("Trabajando")
        
    def dormir(self):
        pass 
"""
    
# Esto anterior está mal porque estoy definiendo y llamando métodos que un objeto no necesita
# ¿Cómo se soluciona esto?
# Dividiendo la interfaz en interfaces más pequeñas

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador, Durmiente, Comedor):
    
    def comer(self):
        print("Comiendo")
        
    def trabajar(self):
        print("Trabajando/laburando")
        
    def dormir(self):
        print("Durmiendo")

class Robot(Trabajador):
    
    def trabajar(self):
        print("Robot Trabajando")


def main():
    persona1 = Humano()
    robot1 = Robot()
    
    persona1.comer()
    persona1.trabajar()
    persona1.dormir()
    
    print("\n")
    
    robot1.trabajar()
main()
