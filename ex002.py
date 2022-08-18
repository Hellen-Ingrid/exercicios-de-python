"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def mudar_valor_lado(self, base, altura):
        self.base = base
        self.altura = altura
        
    def mostrar_valor_lados(self):
        return f'Base: {self.base}, Altura {self.altura}'
    
    def area(self):
        return self.base*self.altura
        
    def perimetro(self):
        return self.base * 2 + self.altura*2
        


if __name__== '__main__':
   b = float(input('Digite a base: '))
   a = float(input('Digite a altura: '))
   ret = Retangulo(b, a)
   print(ret.mostrar_valor_lados())
   print(f'Serão necessários {ret.perimetro()} rodapés para o local.')
   print(f'Serão necessários {ret.area()} pisos para o local.')