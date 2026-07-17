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