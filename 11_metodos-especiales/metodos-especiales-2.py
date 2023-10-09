class Numero:
    def __init__(self, valor):
        self.valor = valor
        
    def __add__(self, otro):
        nuevo_valor = self.valor + otro.valor
        return nuevo_valor
        
        
def main():
    valor_1 = Numero(15)
    valor_2 = Numero(34)
    resultado = valor_1 + valor_2
    print(resultado)
main()