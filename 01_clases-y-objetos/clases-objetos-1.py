"""
La programación orientada a objetos busca optimizar el código para np recurrir en una mala práctica como la
siguiente:

celular1_marca = "Samsung"
celular2_marca = "Apple"
celular3_marca = "Huawei"

celular1_modelo = "S23"
celular2_modelo = "IPhone 15 Pro"
celular3_modelo = "P20 Pro"

celular1_camaraT = "48MP"
celular2_camaraT = "48MP"
celular3_camaraT = "12MP"

celular1_camaraF = "24MP"
celular2_camaraF = "24MP"
celular3_camaraF = "8MP"

print(celular2_camaraF)
"""
"Es tedioso mostrar un sistema de esta forma"


"Para este ejemplo vemos una clase con atributos éstaticos (atributos predefinidos para todos los objetos a crear)"

class Celular():
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"
    
celular_1 = Celular()

print(celular_1) 
"Me va a mostar que es un dato de tipo Object"

print(celular_1.marca)
print(celular_1.modelo)
print(celular_1.camara)
"Acá si me va a mostrar las propiedades de este objeto en específico"
