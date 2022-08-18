"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def mudar_valor_lado(self, lado):
        self.lado = lado
        
    def retornar_valor_lado(self):
        return self.lado
        
    def area(self):
        return self.lado**2
        


if __name__ == '__main__':
    quadrado = Quadrado(4)
    print(quadrado.retornar_valor_lado())
    print(quadrado.area())
    quadrado.mudar_valor_lado(3)
    print(quadrado.retornar_valor_lado())
    print(quadrado.area())
    