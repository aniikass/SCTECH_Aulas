# 1. Crie um programa que peça uma senha ao usuário.
# Enquanto a senha digitada for diferente de 1234,
# o programa deverá solicitar novamente.
# Quando a senha estiver correta, exima: Acesso permitido!

senha = input('Digite a senha: ')

while senha != "1234":
    print('Senha incorreta, tente outra vez.')
    senha = input('Digite a senha: ')

print('Acesso permitido!')

#----------------
# Teodora

# i = 0
# while i < 1:
#     senha = input('Digite a senha: ')
#     if senha == "1234":
#         print("Sistema hackeado!!")
#         i+=1