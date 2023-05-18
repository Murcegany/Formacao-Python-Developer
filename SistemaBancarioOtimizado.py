class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado. Novo saldo: R$ {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado. Novo saldo: R$ {self.saldo}")
        else:
            print("Saldo insuficiente. Operação de saque não realizada.")

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta}: Saldo: R$ {self.saldo}")

    def limite_saque(self):
        limite = self.saldo * 0.1  # Limite de saque de 10% do saldo
        print(f"Limite de saque da conta {self.numero_conta}: R$ {limite}")


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = None

    def cadastrar_conta(self, numero_conta, saldo_inicial=0):
        self.conta = ContaBancaria(numero_conta, saldo_inicial)
        print(f"Conta bancária {numero_conta} cadastrada para o cliente {self.nome}")

    def depositar(self, valor):
        if self.conta:
            self.conta.depositar(valor)
        else:
            print("Cliente não possui conta bancária cadastrada.")

    def sacar(self, valor):
        if self.conta:
            self.conta.sacar(valor)
        else:
            print("Cliente não possui conta bancária cadastrada.")

    def extrato(self):
        if self.conta:
            self.conta.extrato()
        else:
            print("Cliente não possui conta bancária cadastrada.")

    def limite_saque(self):
        if self.conta:
            self.conta.limite_saque()
        else:
            print("Cliente não possui conta bancária cadastrada.")


class Banco:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado no banco.")

    def listar_contas(self):
        print("Lista de contas:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Conta: {cliente.conta.numero_conta if cliente.conta else 'N/A'}")

    def filtrar_usuario(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
