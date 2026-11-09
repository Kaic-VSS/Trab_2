from Enums_Alpha import Severidade, Status

#Verificar se o campo esta preenchido
def ler_campo(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor != "":
            return valor

        print("CAMPO OBRIGATÓRIO!")




def selecionar_severidade():
    while True:
        print("\n=== SEVERIDADE ===")
        print("1 - Baixa")
        print("2 - Média")
        print("3 - Alta")
        print("4 - Crítica")

        opcao = input("Escolha a severidade: ").strip()

        if opcao == "1":
            return Severidade.BAIXA.value

        elif opcao == "2":
            return Severidade.MEDIA.value

        elif opcao == "3":
            return Severidade.ALTA.value

        elif opcao == "4":
            return Severidade.CRITICA.value

        else:
            print("Opção inválida! Escolha de 1 a 4.")



def selecionar_status():
    while True:
        print("\n=== STATUS DE TRATAMENTO ===")
        print("1 - Aberta")
        print("2 - Em tratamento")
        print("3 - Corrigida")
        print("4 - Aceita como risco")

        opcao = input("Escolha o status: ").strip()

        if opcao == "1":
            return Status.ABERTA.value

        elif opcao == "2":
            return Status.EM_TRATAMENTO.value

        elif opcao == "3":
            return Status.CORRIGIDA.value

        elif opcao == "4":
            return Status.ACEITA.value

        else:
            print("Opção inválida! Escolha de 1 a 4.")