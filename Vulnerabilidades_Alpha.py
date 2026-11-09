from Dados_alpha import salvar_ativos
from Validacoes_Alpha import ler_campo
from Enums_Alpha import Severidade, Status
from Validacoes_Alpha import ler_campo, selecionar_severidade, selecionar_status


#Cadastro de Vulnerabilidades
def cadastrar_vulnerabilidade(ativo):
    print("\n=== CADASTRO DE VULNERABILIDADE ===")
    print(f"Equipamento: {ativo['nome']}")

    descricao = ler_campo("Descrição: ")
    categoria = ler_campo("Categoria: ")
    severidade = selecionar_severidade()
    status = selecionar_status()

    nova_vulnerabilidade = {
        "descricao": descricao,
        "categoria": categoria,
        "severidade": severidade,
        "status": status
    }

    if "vulnerabilidades" not in ativo:
        ativo["vulnerabilidades"] = []

    ativo["vulnerabilidades"].append(nova_vulnerabilidade)

    salvar_ativos()
    print("\nVulnerabilidade cadastrada com sucesso!")



#Consultar vulnerabilidades
def consultar_vulnerabilidades(ativo):
    print("\n=== VULNERABILIDADES DO ATIVO ===")
    print(f"Equipamento: {ativo['nome']}")

    vulnerabilidades = ativo.get("vulnerabilidades", [])

    
    if len(vulnerabilidades) == 0:
        print("\nEste ativo não possui vulnerabilidades cadastradas.")
        return

    for numero, vulnerabilidade in enumerate(vulnerabilidades, start=1):
        print(f"\n--- Vulnerabilidade {numero} ---")
        print(f"Descrição: {vulnerabilidade['descricao']}")
        print(f"Categoria: {vulnerabilidade['categoria']}")
        print(f"Severidade: {vulnerabilidade['severidade']}")
        print(f"Status: {vulnerabilidade['status']}")



#atualizar vulnerabilidade
def atualizar_vulnerabilidade(ativo):
    print("\n=== ATUALIZAR VULNERABILIDADE ===")

    vulnerabilidade = selecionar_vulnerabilidade(ativo)

    if vulnerabilidade is None:
        return

    print("\n=== CAMPO PARA ATUALIZAR ===")
    print("1 - Descrição")
    print("2 - Categoria")
    print("3 - Severidade")
    print("4 - Status")
    print("0 - Cancelar")

    opcao = input("Escolha uma opção: ").strip()

    
    if opcao == "1":
        print(f"Descrição atual: {vulnerabilidade['descricao']}")
        novo_valor = ler_campo("Nova descrição: ")
        vulnerabilidade["descricao"] = novo_valor

    elif opcao == "2":
        print(f"Categoria atual: {vulnerabilidade['categoria']}")
        novo_valor = ler_campo("Nova categoria: ")
        vulnerabilidade["categoria"] = novo_valor

    elif opcao == "3":
        print(f"Severidade atual: {vulnerabilidade['severidade']}")
        vulnerabilidade["severidade"] = selecionar_severidade()

    elif opcao == "4":
        print(f"Status atual: {vulnerabilidade['status']}")
        vulnerabilidade["status"] = selecionar_status()

    elif opcao == "0":
        print("Atualização cancelada.")
        return

    else:
        print("Opção inválida!")
        return

    salvar_ativos()
    print("\nVulnerabilidade atualizada com sucesso!")



#remover vulnerabilidade
def remover_vulnerabilidade(ativo):
    print("\n=== REMOVER VULNERABILIDADE ===")

    vulnerabilidade = selecionar_vulnerabilidade(ativo)

    if vulnerabilidade is None:
        return

    print("\n=== VULNERABILIDADE SELECIONADA ===")
    print(f"Descrição: {vulnerabilidade['descricao']}")
    print(f"Severidade: {vulnerabilidade['severidade']}")
    print(f"Status: {vulnerabilidade['status']}")

    while True:
        confirmacao = input(
            "\nDeseja realmente remover esta vulnerabilidade? (s/n): ").strip().lower()

        if confirmacao == "s":
            break

        elif confirmacao == "n":
            print("\nRemoção cancelada.")
            return

        else:
            print("Opção inválida! Digite s ou n.")

        
    ativo["vulnerabilidades"].remove(vulnerabilidade)

    salvar_ativos()

    print("\nVulnerabilidade removida com sucesso!")






#Selecionar vulnerabilidade
def selecionar_vulnerabilidade(ativo):
    vulnerabilidades = ativo.get("vulnerabilidades", [])

    if len(vulnerabilidades) == 0:
        print("\n Este ativo não possui vulnerabilidades cadastradas.")
        return None

    print("\n=== SELECIONAR VULNERABILIDADE ===")
    for numero, vulnerabilidade in enumerate(vulnerabilidades, start=1):
        print(f"{numero} - {vulnerabilidade['descricao']}")

    while True:
        escolha = input("\n Digite o número da vulnerabilidade ou 0 para cancelar: ").strip()
        
        if escolha == "0":
            return None
        if not escolha.isdigit():
            print("Opção inválida! Digite um número válido.")
            continue

        indice = int(escolha) - 1

        if 0 <= indice < len(vulnerabilidades):
            return vulnerabilidades[indice]

        print("Vulnerabilidade não encontrada")
        