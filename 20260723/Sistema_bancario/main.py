# Sistema de Caixa Eletrônico

saldo = 100
extrato = []

def menu():
    print("\n=== SISTEMA CAIXA ELETRÔNICO ===\n")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("5 - Sair")

def consultar_saldo():
    print(f"Seu saldo atual é de: R$ {saldo:.2f}")
    pass # Fecha a função consultar_saldo

def depositar():
    global saldo
    valor = float(input("\nDigite o valor a ser depositado:\n"))
    if valor <= 0:
        saldo += valor
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.\n")
    pass # Fecha a função depositar

def sacar():
    global saldo
    valor = float(input("\nInsira o valor a ser sacado:\n"))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.\n")
    pass # Fecha a função sacar

def extrato():
    print(f"\nExtrato: SEU SALDO É DE "
          f"\nR$ {saldo:.2f}")

def main():
    while True:
        menu()
        opcao = input("\nEscolha uma opção:\n")

        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            extrato()
        elif opcao == "5":
            print("\nAtendimento encerrado.\n")
            break
        else:
            print("\nOpção inválida. Por favor, insira uma opção válida.\n")

main()