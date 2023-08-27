class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola! Estoy hablando un poco\n")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
    
def main():
    roberto = EmpleadoArtista("Roberto", 43, "argentino", "cantar", 120000, "Baufest")
    print(roberto.nombre)
    print(roberto.edad)
    print(roberto.nacionalidad)
    print(roberto.empresa)
    roberto.presentarse()
    
    # ¿Cómo podemos saber si una clase es subclase de otra?
    # Es decir, que herede propiedades de una clase padre
    
    print("\n")
    herencia = issubclass(EmpleadoArtista, Artista)
    print(herencia) # Tiene que retornar true o false (booleano); En este caso true
    
    print("\n")
    herencia2 = issubclass(EmpleadoArtista, Persona)
    print(herencia2)
    
    print("\n")
    herencia3 = issubclass(Persona, Artista)
    print(herencia3)
    
    # ¿Cómo podemos saber si un objeto es una instancia de una clase? => Con isinstance
    # También devuelve un valor booleano
    
    print("\n")
    instancia = isinstance(roberto, EmpleadoArtista)
    print(instancia)
    
    print("\n")
    instancia2 = isinstance(roberto, Artista)
    print(instancia2)
    
    print("\n")
    instancia3 = isinstance(roberto, Persona)
    print(instancia3)
    
    alvaro = Artista("Mago")
    
    print("\n")
    instancia4 = isinstance(alvaro, EmpleadoArtista)
    print(instancia4)
main()