# Código de exemplocompartilhado pelo professor

matricula_cadastrada= "1001"
matricula_cadastrada_01= "1002"
matricula_cadastrada_02= "1003"
matricula_cadastrada_03= "1004"
usuario = ["Usuário Exemplo", "1234", "", "", "", ""]

while True:
    print("\n=== Sistema de Ponto ===")
    print("1 - Login")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        matricula = input("Matrícula: ")
        senha = input("Senha: ")

        if matricula == matricula_cadastrada and senha == usuario[1]:
            while True:
                print("\n--- Menu de", usuario[0], "---")
                print("1 - Registrar ponto")
                print("2 - Ver registros")
                print("0 - Voltar")

                opcao2 = input("Escolha uma opção: ")

                if opcao2 == "1":
                    hora = input("Digite o horário atual (ex: 08:00): ")

                    if usuario[2] == "":
                        usuario[2] = hora
                        print("Entrada registrada às", hora)
                    elif usuario[3] == "":
                        usuario[3] = hora
                        print("Saída para o almoço registrada às", hora)
                    elif usuario[4] == "":
                        usuario[4] = hora
                        print("Retorno do almoço registrado às", hora)
                    elif usuario[5] == "":
                        usuario[5] = hora
                        print("Saída registrada às", hora)
                    else:
                        print("Todos os pontos do dia já foram registrados.")

                elif opcao2 == "2":
                    print("\nRegistro de ponto de", usuario[0])
                    print("Entrada:        ", usuario[2] or "--:--")
                    print("Saída almoço:   ", usuario[3] or "--:--")
                    print("Retorno almoço: ", usuario[4] or "--:--")
                    print("Saída:          ", usuario[5] or "--:--")

                elif opcao2 == "0":
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Matrícula ou senha inválida.")

    elif opcao == "0":
        print("Até mais!")
        break

    else:
        print("Opção inválida.")