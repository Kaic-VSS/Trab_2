from Ativos_Beta import cadastro_ativo, ConsultarATV, AtualizarATV, RemoverATV , selecionar_ativo
from Vulnerabilidades_Beta import cadastrar_vulnerabilidade, consultar_vulnerabilidades, atualizar_vulnerabilidade, remover_vulnerabilidade


def Menu_Principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Menu de Ativos")
        print("2 - Menu de Vulnerabilidades")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            Menu_Ativos()
        elif opcao == "2":
            Menu_Vulnerabilidades()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Escolha de 1 a 2.")
            return  


def Menu_Ativos():
    while True:
        print("\n=== MENU DE ATIVOS ===")
        print("1 - Cadastrar ativo")
        print("2 - Consultar ativos")
        print("3 - Atualizar ativo")
        print("4 - Remover ativo")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastro_ativo()
        elif opcao == "2":
            ConsultarATV()
        elif opcao == "3":
            ativo = selecionar_ativo()

            if ativo is not None:
                AtualizarATV(ativo)

        elif opcao == "4":
            ativo = selecionar_ativo()

            if ativo is not None:
                RemoverATV(ativo)

        elif opcao == "0":
            break
    
        else:
            print("Opção inválida! Escolha de 0 a 4.")


def Menu_Vulnerabilidades():
    while True:
        print("\n=== MENU DE VULNERABILIDADES ===")
        print("1 - Cadastrar vulnerabilidade")
        print("2 - Consultar vulnerabilidades")
        print("3 - Atualizar vulnerabilidade")
        print("4 - Remover vulnerabilidade")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao in ("1", "2", "3", "4"):
            ativo = selecionar_ativo()

            if ativo is None:
                continue

            if opcao == "1":
                cadastrar_vulnerabilidade(ativo)

            elif opcao == "2":
                consultar_vulnerabilidades(ativo)

            elif opcao == "3":
                atualizar_vulnerabilidade(ativo)

            elif opcao == "4":
                remover_vulnerabilidade(ativo)

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")



Menu_Principal()