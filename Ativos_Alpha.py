
import json
from pathlib import Path


# Caminho do arquivo JSON
caminho_json = Path(__file__).parent / "ativos.json"


with open(caminho_json, "r", encoding="utf-8") as arquivo:
    ativos = json.load(arquivo)


# VALIDAR CAMPOS
def ler_campo(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor != "":
            return valor

        print("CAMPO OBRIGATÓRIO!")


# CADASTRO DOS ATIVOS
def cadastro_ativo():
    print("\n=== CADASTRO DE ATIVOS ===")

    # Validar ID e impedir duplicidade
    while True:
        id_ativo = ler_campo("ID do ativo: ")

        if not id_ativo.isdigit() or int(id_ativo) <= 0:
            print("ID inválido! Digite um número inteiro positivo.")
            continue

        id_ativo = int(id_ativo)

        repetido = False

        for ativo in ativos:
            if ativo["id"] == id_ativo:
                repetido = True
                break

        if repetido:
            print("ID já cadastrado! Digite outro.")
            continue

        break

    # Receber informações do ativo
    nome = ler_campo("Nome do ativo: ")
    tipo = ler_campo("Tipo do ativo: ").lower()
    setor = ler_campo("Setor localizado: ")
    responsavel = ler_campo("Responsável pelo ativo: ")
    vulnerabilidade = input("Vulnerabilidade encontrada (se houver): ").strip()

    # Organizar os dados
    novo_ativo = {
        "id": id_ativo,
        "nome": nome,
        "tipo": tipo,
        "setor": setor,
        "responsavel": responsavel,
        "vulnerabilidade": vulnerabilidade
    }

    ativos.append(novo_ativo)

    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(ativos, arquivo, indent=4, ensure_ascii=False)

    print("\n=== ATIVO CADASTRADO ===")

    for campo, valor in novo_ativo.items():
        print(f"{campo.capitalize()}: {valor}")


#consultar cadastro de ativos
def ConsultarATV():
    print("\n=== CONSULTA DE ATIVOS ===")
    print("1 - Pesquisar po ID")
    print("2 - Pesquisar por Nome")
    print("3 - pesquisar po setor")
    print("4 - Pesquisar por Responsável")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        pesquisa = input("Digite o ID do ativo: ").strip()

    elif opcao == "2":
        pesquisa = input("Digite o Nome do ativo: ").strip().lower()

    elif opcao == "3":
        pesquisa = input("Digite o Setor do ativo: ").strip().lower()

    elif opcao == "4":
        pesquisa = input("Digite o Responsável pelo ativo: ").strip().lower()

    else:
        print("Opção inválida!")
        return

    if pesquisa == "":
        print("A pesquisa não pode estar vazia!")
        return

    resultados = []

    for ativo in ativos:
        if opcao == "1":
            if str(ativo["id"]) == pesquisa:
                resultados.append(ativo)
        elif opcao == "2":
            if pesquisa.lower() in ativo["nome"].lower():
                resultados.append(ativo)
        elif opcao == "3":
            if pesquisa.lower() in ativo["setor"].lower():
                resultados.append(ativo)
        elif opcao == "4":
            if pesquisa.lower() in ativo["responsavel"].lower():
                resultados.append(ativo)

    if len(resultados) == 0:
        print("\nNenhum ativo encontrado!")
    else:
        print("\n=== ATIVOS ENCONTRADOS ===")

        for ativo in resultados:
            print(f"\nID: {ativo['id']}")
            print(f"Nome: {ativo['nome']}")
            print(f"Tipo: {ativo['tipo']}")
            print(f"Setor: {ativo['setor']}")
            print(f"Responsável: {ativo['responsavel']}")
            print(f"Vulnerabilidade: {ativo['vulnerabilidade']}")
            print("------------------------")

    if len(resultados) > 0:
        id_escolhido = input(
            "\nDigite o ID para ver detalhes (ou 0 para voltar): "
        ).strip()

        if id_escolhido == "0":
            return

        ativo_selecionado = None

        for ativo in resultados:
            if str(ativo["id"]) == id_escolhido:
                ativo_selecionado = ativo
                break

        if ativo_selecionado is None:
            print("\nID não encontrado nos resultados.")
            return

        print("\n=== DETALHES DO ATIVO ===")
        for campo, valor in ativo_selecionado.items():
            print(f"{campo.capitalize()}: {valor}")

    
        print("\n=== GERENCIAR ATIVO ===")
        print("1 - Atualizar ativo")
        print("2 - Remover ativo")
        print("0 - Voltar")

        acao = input("Escolha uma opção: ").strip()

        if acao == "1":
            AtualizarATV(ativo_selecionado)

        elif acao == "2":
            RemoverATV(ativo_selecionado)

        elif acao == "0":
            return

        else:
            print("Opção inválida!")



#atualizar cadastro de ativos
def AtualizarATV(ativo):
    print("\n=== ATUALIZAÇÃO DE ATIVO ===")
    print(f"Equipamento selecionado: {ativo['nome']}")

    print("1 - Alterar nome")
    print("2 - Alterar tipo")
    print("3 - Alterar setor")
    print("4 - Alterar responsável")
    print("0 - Cancelar")

    opcao = input("Escolha o campo: ").strip()
    
    if opcao == "1":
        campo = "nome"
    elif opcao == "2":
        campo = "tipo"
    elif opcao == "3":
        campo = "setor"
    elif opcao == "4":
        campo = "responsavel"
    elif opcao == "0":
        return
    else:
        print("Opção inválida!")
        return
    
    
    print(f"\nValor atual: {ativo[campo]}")
    novo_valor = ler_campo("Digite o novo valor: ")
    ativo[campo] = novo_valor
    salvar_ativos()
    print("\nAtivo atualizado com sucesso!")




#remover cadastro de ativos
def RemoverATV(ativo):
    print("\n=== REMOVER ATIVO ===")
    print(f"ID: {ativo['id']}")
    print(f"Nome: {ativo['nome']}")

    confirmacao = input("Deseja realmente remover este ativo? (s/n): ").strip().lower()

    if confirmacao == "s":
        ativos.remove(ativo)
        salvar_ativos()
        print("\nAtivo removido com sucesso!")

    else:
        print("\nRemoção cancelada.")


#salvar ativos atualizados no arquivo JSON
def salvar_ativos():
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(ativos, arquivo, indent=4, ensure_ascii=False)
