class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nuevo_nombre(self, new_nombre):
        self.__nombre = new_nombre


dalto = Persona("Lucas", 21)

# La convención para acceder a un atributo muy privado es mediante un método
## Para este caso: get_nombre()
### Este tipo de funciones son getters => para acceder a un dato/atributo

nombre = dalto.get_nombre()
print(nombre)
# print(dalto.__nombre) # Así no se puede acceder

# Aplicando set y get
dalto.set_nuevo_nombre("Pepito")
nombre = dalto.get_nombre()
print(nombre)

