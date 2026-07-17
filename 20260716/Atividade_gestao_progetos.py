# Atividade Gestão de Projetos - 16/07/2026
# Criar um conversor de Celsius para Fahrenheit (e o inverso também funcionar)

# Nota de boas-vindas
print("\n\nBEM-VINDO AO MARAVILHOSO CONVERSOR DE TEMPERATURAS!")

# Declarar a variável proceed para controle de loop
proceed = "1"

# Início do loop principal, com a definição do escopo de conversão.
while proceed == "1":

# Instruções iniciais para seguimento na conversão (from - to)
    print(
        "\nVamos lá, selecione o número que melhor descreve o que você quer fazer:\n"
        "\n1 - Converter de Celsius para Fahrenheit"
        "\n2 - Converter de Fahrenheit para Celsius\n"
    )

# Entrada da seleção
    select = input()

# Warning de seleção inválida, caso não esteja no range sugerido
    while select not in ["1", "2"]:
        print("\nDigitou errado, hein? Aqui não passa nada!")
        select = input("Por favor, selecione apenas 1 ou 2:\n")

# Condicional de Celsius para Fahrenheit
    if select == "1":
        print("\nQual valor deve ser convertido para Fahrenheit?")
        value = float(input())

        print("\nConvertendo...")
# Cálculo da conversão de C -> F
        C_to_F = (value * 9/5) + 32

# Resultado da conversão 1
        print(f"{value} °C = {C_to_F:.1f} °F")

# Cálculo da conversão de F -> C
    elif select == "2":
        print("\nQual valor deve ser convertido para Celsius?")
        value = float(input())

        print("\nConvertendo...")
# Cálculo da conversão de F -> C
        F_to_C = (value - 32) * (5/9)

# Resultado da conversão 2
        print(f"{value} °F = {F_to_C:.1f} °C")

# Deseja continuar? Input do usuário
    print(
        "\nE aí, Querubim... quer converter mais algum valor?"
        "\nDigite 1 para SIM e 2 para NÃO.\n"
    )

#Entrada do usuário
    proceed = input()

    while proceed not in ["1", "2"]:
        proceed = input("Opção inválida. Digite apenas 1 para SIM ou 2 para NÃO:\n")

print("\nShow de bolitas! Então até a próxima, xau!")