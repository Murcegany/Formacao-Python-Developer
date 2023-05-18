class Banco:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato(self):
        print(f"Saldo atual: R$ {self.saldo}")


def exibir_menu():
    print("===== Menu =====")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    print("================")


banco = Banco()

while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor = int(input("Digite o valor a ser depositado: "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = int(input("Digite o valor a ser sacado: "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        print("Saindo do sistema bancário...")
        break
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")

    print()  # Linha em branco para separar as ações

