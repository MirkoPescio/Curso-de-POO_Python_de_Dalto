"""
Ejercicio 1

Crear una clase Estudiante. Asignarle los atributos: Nombre, Edad y Grado.
Aplicarle un método estudiar() tal que muestre por consola 'el estudiante (nombre) está estudiando'. Usar el método.
Se debe interactuar con el usuario y este debe brindar los atributos.
Al escribir "estudiar", utilizar el método estudiar()
"""

# Mi solución

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f"El/la estudiante {self.nombre} está estudiando")
    
def main():
    estudianteUsuario = Estudiante(
        input("Ingrese su nombre: "),
        int(input("Ingrese su edad: ")),
        input("Ingrese su grado/curso: ")
    )
    estudiando = input("Está estudiando? (estudiando/no): ")
    
    print(estudianteUsuario.nombre)
    print(estudianteUsuario.edad)
    print(estudianteUsuario.grado)
    
    if (estudiando.lower() == "estudiando"):
        estudianteUsuario.estudiar()
main()

# Solución de Dalto

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("Estudiando...")
        
nombre = input("Digame su nombre: ")
edad = input("Ahora su edad: ")
grado = input("Por último, su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
    """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        
