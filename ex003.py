"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
        
    def envelhecer(self):
         self.idade += 1
         return self.idade
        
    def engordar(self):
         self.peso += 0.5
         return self.peso
        
    def emagrecer(self):
          self.peso -= 0.5
          return self.peso
        
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5
            return self.altura
        else:
            return self.altura
            
            
if __name__=='__main__':
    hellen = Pessoa(nome='Hellen', idade=21, altura=1.50, peso=51)
    print(f'{hellen.nome} tem: ')
    print(f'{hellen.idade} anos')
    print(f'{hellen.peso} kg')
    print(f'{hellen.altura} m')
    print('-------------------------------')
    hellen.envelhecer()
    hellen.engordar()
    hellen.crescer()
    print(f'{hellen.nome} tem: ')
    print(f'{hellen.idade} anos')
    print(f'{hellen.peso} kg')
    print(f'{hellen.altura} m')
    print('-------------------------------')
    hellen.envelhecer()
    hellen.emagrecer()
    hellen.crescer()
    print(f'{hellen.nome} tem: ')
    print(f'{hellen.idade} anos')
    print(f'{hellen.peso} kg')
    print(f'{hellen.altura} m')
    