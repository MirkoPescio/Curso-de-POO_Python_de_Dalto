"""
Ejemplo para Polimorfismo de cohersión
"""

num1 = 3
num2 = 4.7

resultado = num1 + num2

print(resultado)
print(type(resultado))

# En Python, al ser de tipado dinámico, a pesar de que 2 datos sean de diferente tipo, el comportamiento de las tareas
# son iguales en éste lenguaje

def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
        
lista1 = [1, 2, 3, 4]
lista2 = ["Máquina", "cómo", "andás"]

recorrer(lista1)
print("\n")
recorrer(lista2)

# Esto es el POLIMORFISMO. MISMA FUNCION <==> DIFERENTE/S DATO/S
