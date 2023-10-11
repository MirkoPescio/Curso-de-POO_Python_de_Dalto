"""
Principio LSP => principio de sustitución de Liskov

Buscar: científica Barbara Liskov

Este principio establece que las clases derivadas tienen que ser sustituibles por sus clases base
"""

""" class Ave():
    def volar(self):
        return "Ave volando"
    
class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"
    
def hacer_volar(ave = Ave):
    return ave.volar()

def main():
    print(hacer_volar(Pinguino()))
main() """

# Reconstruímos el código anterior aplicando el principio de Liskov

class Ave():
    pass

class AveVoladora():
    def volar(self):
        return "Ave volando"

class AveNoVoladora():
    pass

def main():
    pass
main()
