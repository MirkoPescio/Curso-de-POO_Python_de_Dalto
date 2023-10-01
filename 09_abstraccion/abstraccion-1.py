"""
Abstracción:

En su concepto más básico significa, manejar la complejidad ocultando todos los detalles innecesarios al programador
y/o al usuario proporcionandoles las funcionalidades más relevantes

CREAR UNA INTERFAZ SIMPLE QUE OCULTE LA INTERFAZ COMPLEJA
"""

class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido")
        
    def conducir(self):
        if (self._estado == "apagado"):
            self.encender()
        print("Conduciendo el auto")
        
def main():
    mi_auto = Auto()
    mi_auto.conducir()
main()
