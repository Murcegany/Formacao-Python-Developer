from abc import ABC, abstractmethod
from datetime import datetime
#importanto bilbioteca para date e classe abstrata

#Interface Transacao
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
    
#Classes deposito e Saque como filhas da interface Transacao
class Deposito(Transacao):
    def __init__(self):
        self.__valor = 0.0

    def registrar(self, conta):
        print("Registrando depósito...")      

    def depositar(self, conta, valor):
        self.__valor = float(valor)
        print(f"Realizando depósito de R${self.__valor:.2f} na conta {conta.numero}")    

    def get_valor(self):
        return self.__valor

class Saque(Transacao):
    def __init__(self):
        self.__valor = 0.0

    def registrar(self, conta):
        print("Saque registrado.") 

    def sacar(self, conta, valor):
        self.__valor = float(valor)
        print(f"Realizando saque de R${self.__valor:.2f} na conta {conta.numero}") 

    def get_valor(self):
        return self.__valor
    
# Classes PessoaFisica como filhas da Cliente
class Cliente:
    def __init__(self, endereco):
        self.__endereco = endereco
        self.__contas = []
        
    @classmethod
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def get_endereco(self):
        return self.__endereco

    def get_contas(self):
        return self.__contas

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_data_nascimento(self):
        return self.__data_nascimento
    
# Classe Histórico implementada com Conta+Interface
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        
# ContaCorrente implementa Conta
class ContaCorrente:
    def __init__(self, limite, limite_saque):
        self.__limite = limite
        self.__limite_saque = limite_saque

    def get_limite(self):
        return self.__limite

    def get_limite_saque(self):
        return self.__limite_saque

    def set_limite(self, limite):
        self.__limite = limite

    def set_limite_saque(self, limite_saque):
        self.__limite_saque = limite_saque

class Conta(ContaCorrente):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saque):
        super().__init__(limite, limite_saque)
        self.__saldo = saldo
        self.__numero = numero
        self.__agencia = agencia
        self.__cliente = cliente
        self.__historico = historico

    def saldo(self):
        return self.__saldo

    # Iniciando valores para a criação de uma nova conta
    def nova_conta(cliente, numero):
        agencia = "Agência Padrão"  # Valor padrão para a agência
        historico = Historico()  # Cria um novo histórico para a conta
        limite = 0.0
        limite_saque = 0.0
        return Conta(0.0, numero, agencia, cliente, historico, limite, limite_saque)

    def sacar(self, valor):
        if self.__saldo + self.get_limite() >= valor and self.get_limite_saque() >= valor:
            self.__saldo -= valor
            self.__historico.adicionar_transacao(Saque())
            return True
        return False

    def depositar(self, valor):
        self.__saldo += valor
        self.__historico.adicionar_transacao(Deposito())
        return True
    
# Criando uma classe menu para a exibição do sistema bancário
class Menu:
    def __init__(self): # Menu encapsula a lógica do menu a função exibir_menu()
        self.opcoes = { # Cada opção do menu armazenados em um dicionário 
            "1": self.criar_nova_conta,
            "2": self.realizar_deposito,
            "3": self.realizar_saque,
            "4": self.verificar_saldo,
            "0": self.sair
        }
    # Exibição do menu
    def exibir_menu(self):
        print("===== Sistema Bancário =====")
        print("1. Criar nova conta")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Verificar saldo")
        print("0. Sair")
        print("============================")
        
    # Metódo para procurar uma conta
    def encontrar_conta(cliente, numero_conta):
        for conta in cliente.get_contas():
            if conta.numero == numero_conta:
                return conta
        return None
    
    # Metódo para criar uma nova conta
    def criar_nova_conta(self):        
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente (formato: DD/MM/AAAA): ")
        endereco = input("Digite o endereço do cliente: ")

        pessoa_fisica = PessoaFisica(cpf, nome, data_nascimento, endereco)
        cliente = Cliente(pessoa_fisica)

        numero_conta = input("Digite o número da conta: ")
        agencia = input("Digite a agência da conta: ")

        saldo = 0.0  # Definindo saldo inicial para a nova conta
        historico = Historico()  # Criando um novo histórico para a conta
        limite = 0.0
        limite_saque = 0.0

        conta = Conta(saldo, numero_conta, agencia, cliente, historico, limite, limite_saque)
        cliente.adicionar_conta(conta)

        print("Nova conta criada com sucesso!")
        
    # Metódo para realizar um deposito
    def realizar_deposito(self):
        numero_conta = input("Digite o número da conta: ")
        valor_deposito = float(input("Digite o valor do depósito: "))

        conta = self.encontrar_conta(numero_conta)
        if conta:
            if valor_deposito > 0:
                conta.depositar(valor_deposito)
                print("Depósito realizado com sucesso!")
            else:
                print("Valor inválido para depósito.")
        else:
            print("Conta não encontrada.")


    # Metódo para realizar um saque
    def realizar_saque(self):
        numero_conta = input("Digite o número da conta: ")
        valor_saque = float(input("Digite o valor do saque: "))

        conta = self.encontrar_conta(numero_conta)
        if conta:
            if valor_saque > 0:
                if conta.saldo() >= valor_saque and conta.get_limite_saque() >= valor_saque:
                    conta.sacar(valor_saque)
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo insuficiente ou limite de saque excedido.")
            else:
                print("Valor inválido para saque.")
        else:
            print("Conta não encontrada.")

    # Metódo para verificar o saldo
    def verificar_saldo(self):
        numero_conta = input("Digite o número da conta: ")

        conta = self.encontrar_conta(numero_conta)
        if conta:
            saldo = conta.saldo()
            print(f"Saldo da conta {conta.numero}: R${saldo:.2f}")
        else:
            print("Conta não encontrada.")
            
     # Metódo para sair do menu 
    def sair(self):
        print("Saindo do sistema...")
        
    # Metódo para executar o menu
    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Digite a opção desejada: ")

            if opcao in self.opcoes:
                funcao = self.opcoes[opcao]
                funcao()
            else:
                print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    menu = Menu()
    menu.executar()
