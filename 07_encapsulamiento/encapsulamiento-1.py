"""
Encapsulamiento: su concepto básico es el de proteger las clases, y por ende, los datos.
"""

class MiClase:
    def __init__(self):
        self.atributo_privado = "Valor"
        
objeto = MiClase()
# El desarrollador sabe que no debe acceder a este atributo, pero puede
print(objeto.atributo_privado)

# Atributo MUY PRIVADO, según Dalto:
## consiste en poner __ a un atributo:

class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor"
    def __hablar(self):
        return "Hola, ¿cómo estás?"
        
objeto = MiClase()
print(objeto.__atributo_privado)
# Me va a dar error porque Python sabe que es un atributo privado 

## También sirve para métodos
print(objeto.__hablar()) # Tampoco lo va a ejecutar


### La convención sería la siguiente:

class SegundaClase:
    def __init__(self, valorPublico, valorPrivado, valorMuyPrivado):
        self.valorPublico = valorPublico
        self._valorPrivado = valorPrivado
        self.__valorMuyPrivado = valorMuyPrivado

