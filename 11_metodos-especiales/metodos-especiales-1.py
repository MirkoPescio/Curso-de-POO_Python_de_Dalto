class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Método especial para devolver textos en una clase
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
def main():
    mirko = Persona("Mirko", 24)
    print(mirko)
    print("\n")
    repre = repr(mirko)
    resultado = eval(repre)
    print(resultado)
main()