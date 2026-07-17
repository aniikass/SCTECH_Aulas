# 1. Crie um programa que peça uma senha ao usuário.
# Enquanto a senha digitada for diferente de 1234,
# o programa deverá solicitar novamente.
# Quando a senha estiver correta, exima: Acesso permitido!

senha = int(input('Digite a senha: '))

while senha != 1234:
    print('Senha incorreta, tente outra vez.')
    senha = int(input('Digite a senha: '))

print('Acesso permitido!')


# 2. Crie um programa que solicite ao usuário 5 números inteiros
# utilizando o laço while. Ao final, exiba a soma
# de todos os valores digitados.

contador = 1
soma = 0

while contador <= 5:
    numero = int(input(f'Digite o {contador}º número: '))
    soma = soma + numero
    contador = contador + 1

print(f'A soma dos números é: {soma}')