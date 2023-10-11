"""
Ultimo principio SOLID => principio de inversión de dependencias

Este principio establece 2 cosas:

1) Los módulos de alto nivel no tienen que depender de los de bajo nivel, sino que los 2 tienen que depender de las
   abstracciones
2) Las abstracciones no deben depender de los detalles, sino que los detalles deben depender de las abstracciones
   Es decir, no tenemos que depender de implementaciones específicas
"""

""" 
class Diccionario():
    def varificar_palabra(self, palabra):
        # Lógica para verificar palabras
        pass
    
class CorrectorOrtografico():
    def __init__(self):
        self.diccionario = Diccionario()
        
    def corregir_texto(self, texto):
        # Usamos el diccionario para corregir el texto
        pass 
"""

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    
    @abstractmethod
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si están en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras desde el servicio web
        pass

class CorrectorOrtografico():
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        # Usamos el verificador para corregir texto
        pass    

"""
Es decir, como Verificador es una clase abstracta, tenemos todos los métodos que necesitamos ahí mismo, si tiene más
métodos, como por ejemplo: buscar_similares() o corregir_ortografia() o agregar_acento() podemos quedarnos tranquilos
de que podemos seguir usando los mismos métodos que tenga el verificador, porque al ser una subclase tendría que poder
hacer todo lo que hace la clase base (Principio de sustitución de Liskov)
"""

def main():
    corrector = CorrectorOrtografico(Diccionario())
main()
