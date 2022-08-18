"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

class ContaCorrente:
    def __init__(self, conta, nome, saldo=0.0):
        self.saldo = saldo
        self.nome = nome
        self.conta = conta

    def alterar_nome(self, nome):
        self.nome = nome
        return self.nome

    def deposito(self, saldo):
        self.saldo = saldo
        return saldo

    def saque(self, valor_saque):
        self.saldo = self.saldo - valor_saque
        return self.saldo


if __name__ == '__main__':
    n = str(input('Digite seu nome: '))
    c = int(input('Número da Conta: '))
    try:
        s = float(input('Digite seu saldo (OPCIONAL): R$'))
    except:
        s = 0
    conta_1 = ContaCorrente(nome=n, conta=c, saldo=s)
    print(f'Conta: {conta_1.conta}, Titular: {conta_1.nome}, Saldo: R${conta_1.saldo:.2f}')
    resp = str(input('Deseja realizar um saque [S/N] ? '))
    if resp in 'Ss':
        vs = float(input('Valor do saque: R$'))
        if conta_1.saldo < vs:
            print('SAQUE INDISPONÍVEL! VOCÊ NÂO TEM SALDO SUFICIENTE.')
            print('TENHA UM BOM DIA!')
        else:
            conta_1.saque(vs)
            print(f'Você fez um saque de R${vs:.2f}. Seu Saldo agora é de R${conta_1.saldo:.2f}')
            print('TENHA UM BOM DIA!')
    else:
        print('TENHA UM BOM DIA!')
