"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""


class Tv:
    def __init__(self, canal=1):
        self.canal = canal
        self.volume = 15

    def aumentar_volume(self):
        self.volume += 1
        self.volume = min(self.volume, 100)

    def diminuir_volume(self):
        self.volume -= 1
        self.volume = max(0, self.volume)

    def mudar_canal(self, canal):
        self.canal = canal
        return self.canal


if __name__ == '__main__':
    televisao = Tv()
    print(30 * '-')
    print(f'{"TELEVISÃO":^30}')
    while True:
        print(30 * '-')
        print(f'Você está no canal {televisao.canal}. O volume está em {televisao.volume}')
        print("""O QUE DESEJA FAZER? 
1 - Mudar Canal
2 - Aumentar volume
3 - Diminuir volume""")
        print(30 * '-')
        opcao = int(input('Opção: '))
        if opcao == 1:
            c = int(input('Qual canal você quer acessar: '))
            televisao.mudar_canal(c)
            print(f'Canal: {televisao.canal}')
        elif opcao == 2:
            televisao.aumentar_volume()
            print(f'Volume: {televisao.volume}')
        elif opcao == 3:
            televisao.diminuir_volume()
            print(f'Volume: {televisao.volume}')
        resp = str(input('Quer continuar assistindo [S/N] ? '))
        if resp in 'Nn':
            print(f'Você está no canal {televisao.canal}. O volume está em {televisao.volume}')
            break
    print('DESLIGANDO A TV')
