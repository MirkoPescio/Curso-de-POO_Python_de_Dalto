class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
        
class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")

"""
El orden de prioridad de métodos en las clases es la siguiente:
Si llamo al método hablar() de la clase D va a ejecutarlo desde la misma clase => D. Hasta ahí no hay ninguna complicación
Ahora si hablar() no estuviera en la clase D, ¿Cuál ejecutaria? ¿El de la clase B, C o A?
Ejecutaría el método de la clase que herede primero, en este caso, B => 'Hola desde B'.
Si la clase B no tuviera el método hablar, ejecutaría la siguiente => C => 'Hola desde C'
Y por último si D, B ni C tuviesen el método hablar() ejecuta el método en la clase de mayor gerarquía => A => 'Hola 
desde A'
"""

def main():
    d = D()
    
    d.hablar()
    
    # También para saber el orden de gerarquía entre clases podemos aplicar lo siguiente:
    
    print(D.mro())
    
    A.hablar(d)
    B.hablar(d)
    C.hablar(d)
main()

