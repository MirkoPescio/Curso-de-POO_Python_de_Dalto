"""
Decoradores

Un concepto de Python que no se vió en el curso anterior, no porque sea obligatorio, pero que es muy útil saberlo
"""

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return funcion_modificada

def saludo():
    print("Hola Dalto!!")
    
# def main():
#     saludo_modificado = decorador(saludo)
#     saludo_modificado()
# main()

"""
Basicamente es agregar funcionalidades/ejecuciones antes y después de una función.

Otra forma de ejecutarlo es la siguiente:
"""

def main():
    @decorador
    def saludo():
        print("Hola Dalto, ¿cómo andás?")
    saludo()
main()
