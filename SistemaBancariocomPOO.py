class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class ContaBancaria:
    limite_saques = 3
    saque_maximo = 500

    def __init__(self, numero, usuario):
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor < 100:
            print("\nValor mínimo para depósito é R$ 100,00.")
        else:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito realizado! Saldo atual: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if self.numero_saques >= ContaBancaria.limite_saques:
            print("\nNúmero máximo de saques diários atingido.")
        elif valor > ContaBancaria.saque_maximo:
            print(f"\nValor máximo para saque é R$ {ContaBancaria.saque_maximo:.2f}")
        elif valor > self.saldo:
            print("\nSaldo insuficiente.")
        else:
            self.numero_saques += 1
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"\nSaque realizado! Saldo atual: R$ {self.saldo:.2f} | Saques restantes: {ContaBancaria.limite_saques - self.numero_saques}")

    def mostrar_extrato(self):
        print("\n========== EXTRATO ==========")
        if self.extrato:
            print(self.extrato)
        else:
            print("Nenhuma movimentação realizada.")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=============================")

    def __str__(self):
        return f"Conta: {self.numero} | Usuário: {self.usuario.nome} | CPF: {self.usuario.cpf}"


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.conta_logada = None

    def cadastrar_usuario(self):
        cpf = input("Digite o CPF (somente números): ")
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)

        if usuario:
            print("\nUsuário já cadastrado!")
            return

        nome = input("Digite o nome completo: ")
        data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Digite o endereço (logradouro, número, bairro, cidade/UF, CEP): ")

        novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        print("\nUsuário cadastrado com sucesso!")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)

        if not usuario:
            print("\nUsuário não encontrado. Cadastre primeiro.")
            return

        numero_conta = f"{len(self.contas)+1:04d}"
        conta = ContaBancaria(numero_conta, usuario)
        self.contas.append(conta)
        self.conta_logada = conta
        print(f"\nConta criada com sucesso! Número da conta: {numero_conta}")
        print(f"Agora você está usando a conta {conta.numero}.")

    def listar_contas(self):
        print("\n========== CONTAS ==========")
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        else:
            for conta in self.contas:
                print(conta)
        print("=============================")

    def menu(self):
        menu = """
========== BANCO ========== 
Bem vindo ao nosso sistema bancário!
Escolha uma das opções abaixo:
===========================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Usuário
[5] Criar Conta
[6] Listar Contas
[7] Sair
===========================
Digite a opção desejada: """

        while True:
            opcao = input(menu)

            if opcao in ["1", "2", "3"] and not self.conta_logada:
                print("\nVocê precisa cadastrar um usuário e criar uma conta antes de usar essa opção.")
                continue

            if opcao == "1":
                valor = float(input("Valor para depósito: "))
                self.conta_logada.depositar(valor)

            elif opcao == "2":
                valor = float(input("Valor para saque: "))
                self.conta_logada.sacar(valor)

            elif opcao == "3":
                self.conta_logada.mostrar_extrato()

            elif opcao == "4":
                self.cadastrar_usuario()

            elif opcao == "5":
                self.criar_conta()

            elif opcao == "6":
                self.listar_contas()

            elif opcao == "7":
                print("\nObrigado por usar nosso banco. Até mais!")
                break

            else:
                print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    banco = Banco()
    banco.menu()
