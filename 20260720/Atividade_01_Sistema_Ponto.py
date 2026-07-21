# INTRUÇÕES
# Crie um sistema onde existe 01 matriz e 04 escolas
# Objetivo: Gestão de pontos
# Entradas: 
#   01 - Login
#   02 - Senha
#   03 - Horário de Entrada
#   04 - Horário da Saída do Almoço
#   05 - Horário de Retorno do Almoço
#   06 - Horário de Saída
# Condições:
#   01 → Toda vez quando o sistema for pesquisar a matrícula, deve checar o próximo seguimento.
#   02 → Não a dicionar o horário, apenas matrícula e senha.
#   03 → Sistema dependente: Só pode imputar um novo dado se o dado anterior já estiver preenchido.
#   04 → Só pode almoçar entre 11-15h. 
#        Antes ou depois, não aceita horário de almoço. 
#        Se não sair para o almoço, apenas bate a saída da empresa.

print("\n=== SISTEMA DE GESTÃO DE PONTO ===\n")

matriculas = ["1001", "1002", "1003"]
senhas = ["1234", "0202", "2020"]


def validar_horario(mensagem):
    horario = input(mensagem)

    while len(horario) != 4 or not horario.isdigit():
        horario = input(
            "Horário inválido. Digite no formato HHMM (exemplo: 0730): "
        )

    return int(horario)


def formatar_horario(horario):
    if horario == "-":
        return "-"
    horario = f"{horario:04d}"
    return horario[:2] + ":" + horario[2:]


sistema = True

while sistema:

    print("\n--- LOGIN ---")

    login = input("Digite sua matrícula: ")

    while login not in matriculas:
        login = input("Matrícula não encontrada. Digite novamente: ")

    indice = matriculas.index(login)

    senha = input("Digite sua senha: ")

    while senha != senhas[indice]:
        senha = input("Senha incorreta. Digite novamente: ")

    print("\nLogin realizado com sucesso!")

    # ==========================
    # 01 - ENTRADA
    # ==========================

    entrada = validar_horario(
        "\nDigite o horário de entrada (HHMM): "
    )

    if entrada < 600 or entrada > 800:

        print("\nEntrada fora do horário permitido.")
        print("Procure o RH para justificar o horário.")
        print("O RH realizará o registro manualmente.")

        saida_almoco = "-"
        retorno = "-"
        saida = "-"
        status = "Pendente com o RH"

    else:

        # ==========================
        # 02 - SAÍDA PARA ALMOÇO
        # ==========================

        saida_almoco_input = validar_horario(
            "\nDigite o horário de saída para almoço (HHMM): "
        )

        if saida_almoco_input < 1100 or saida_almoco_input > 1500:

            # Não é almoço, é saída definitiva

            saida_almoco = "-"
            retorno = "-"
            saida = saida_almoco_input
            status = "Registrado como saída"

            print("\nHorário fora do período de almoço.")
            print("Registrado como saída do expediente.")

        else:

            saida_almoco = saida_almoco_input

            # ==========================
            # 03 - RETORNO DO ALMOÇO
            # ==========================

            retorno_input = validar_horario(
                "\nDigite o horário de retorno do almoço (HHMM): "
            )

            if retorno_input > 1500:

                # Retorno inválido

                saida_almoco = "-"
                retorno = "-"
                saida = saida_almoco_input
                status = "Expediente encerrado"

                print("\nRetorno após às 15:00.")
                print("Expediente encerrado automaticamente.")

            else:

                retorno = retorno_input

                # ==========================
                # 04 - SAÍDA
                # ==========================

                saida = validar_horario(
                    "\nDigite o horário de saída (HHMM): "
                )

                status = "Registrado"

    # ==========================
    # RESUMO
    # ==========================

    print("\n===== RESUMO DO REGISTRO =====")
    print(f"Matrícula..............: {login}")
    print(f"Entrada................: {formatar_horario(entrada)}")
    print(f"Saída para almoço......: {formatar_horario(saida_almoco)}")
    print(f"Retorno almoço.........: {formatar_horario(retorno)}")
    print(f"Saída..................: {formatar_horario(saida)}")
    print(f"Status.................: {status}")

    continuar = input(
        "\nDeseja realizar outro registro? (S/N): "
    ).upper()

    while continuar not in ["S", "N"]:
        continuar = input(
            "Digite apenas S ou N: "
        ).upper()

    if continuar == "N":
        sistema = False
        print("\nSistema encerrado.")