from Dados_Beta import ativos, salvar_ativos
from Validacoes_Beta import ler_campo
from Enums_Beta import Equipamento, TipoAtivo, criar_equipamento
from Vulnerabilidades_Beta import (
    atualizar_vulnerabilidade,
    cadastrar_vulnerabilidade,
    consultar_vulnerabilidades,
    remover_vulnerabilidade
)



# CADASTRO DOS ATIVOS
def cadastro_ativo():
    print("\n=== CADASTRO DE ATIVOS ===")

    # Validar ID
    while True:
        id_ativo = ler_campo("ID do ativo: ")

        if not id_ativo.isdigit() or int(id_ativo) <= 0:
            print("ID inválido! Digite um número inteiro positivo.")
            continue

        id_ativo = int(id_ativo)

        repetido = False

        for ativo in ativos:
            if ativo.id == id_ativo:
                repetido = True
                break

        if repetido:
            print("ID já cadastrado! Digite outro.")
            continue

        break

    # Informações do equipamento
    nome = ler_campo("Nome do ativo: ")
    print("\n=== TIPO DE ATIVO ===")
    for categoria in TipoAtivo:
        print(f"{categoria.value} - {categoria.descricao}")
    while True:
        escolha_tipo = ler_campo("Código do tipo: ")
        try:
            tipo = TipoAtivo.interpretar(escolha_tipo)
            break
        except ValueError:
            print("Tipo inválido! Escolha de 1 a 4.")
    setor = ler_campo("Setor localizado: ")
    responsavel = ler_campo("Responsável pelo ativo: ")

    # Criar equipamento
    novo_ativo = criar_equipamento(
        id_ativo,
        nome,
        tipo,
        setor,
        responsavel
     )

    # Cadastrar primeira vulnerabilidade
    print("\nCadastre a primeira vulnerabilidade do ativo:")
    cadastrar_vulnerabilidade(novo_ativo, salvar=False)

    # Cadastrar outras vulnerabilidades, se desejar
    while True:
        resposta = input(
            "\nDeseja cadastrar outra vulnerabilidade? (s/n): "
        ).strip().lower()

        if resposta == "s":
            cadastrar_vulnerabilidade(novo_ativo, salvar=False)

        elif resposta == "n":
            break

        else:
            print("Opção inválida! Digite s ou n.")

    # Salvar somente após finalizar o cadastro
    ativos.append(novo_ativo)
    salvar_ativos()

    print("\n=== ATIVO CADASTRADO COM SUCESSO ===")
    print(f"ID: {novo_ativo.id}")
    print(f"Nome: {novo_ativo.nome}")
    print(f"Vulnerabilidades cadastradas: {len(novo_ativo.vulnerabilidades)}")  



#consultar cadastro de ativos
def ConsultarATV():
    print("\n=== CONSULTA DE ATIVOS ===")
    print("1 - Pesquisar por ID")
    print("2 - Pesquisar por Nome")
    print("3 - Pesquisar por Setor")
    print("4 - Pesquisar por Responsável")

    opcao = input("Escolha uma opção: ").strip()

    # Escolher o tipo de pesquisa
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

    # Impedir pesquisa vazia
    if pesquisa == "":
        print("A pesquisa não pode estar vazia!")
        return

    # Procurar equipamentos
    resultados = []

    for ativo in ativos:
        if opcao == "1":
            if str(ativo.id) == pesquisa:
                resultados.append(ativo)

        elif opcao == "2":
            if pesquisa in ativo.nome.lower():
                resultados.append(ativo)

        elif opcao == "3":
            if pesquisa in ativo.setor.lower():
                resultados.append(ativo)

        elif opcao == "4":
            if pesquisa in ativo.responsavel.lower():
                resultados.append(ativo)

    # Verificar resultados
    if len(resultados) == 0:
        print("\nNenhum ativo encontrado!")
        return

    print("\n=== ATIVOS ENCONTRADOS ===")

    for ativo in resultados:
        print(f"\nID: {ativo.id}")
        print(f"Nome: {ativo.nome}")
        print(f"Tipo: {ativo.tipo}")
        print(f"Setor: {ativo.setor}")
        print(f"Responsável: {ativo.responsavel}")
        print(f"Descrição técnica: {ativo.descricao_tecnica()}")
        print("------------------------")

    # Selecionar equipamento
    id_escolhido = input(
        "\nDigite o ID para ver detalhes (ou 0 para voltar): "
    ).strip()

    if id_escolhido == "0":
        return

    ativo_selecionado = None

    for ativo in resultados:
        if str(ativo.id) == id_escolhido:
            ativo_selecionado = ativo
            break

    if ativo_selecionado is None:
        print("\nID não encontrado nos resultados.")
        return

    # Mostrar detalhes
    print("\n=== DETALHES DO ATIVO ===")

    for campo, valor in ativo_selecionado.para_dicionario().items():
        print(f"{campo.capitalize()}: {valor}")

    # Gerenciar equipamento selecionado
    print("\n=== GERENCIAR ATIVO ===")
    print("1 - Atualizar ativo")
    print("2 - Remover ativo")
    print("3 - Cadastrar vulnerabilidade")
    print("4 - Consultar vulnerabilidades")
    print("5 - Atualizar vulnerabilidade")
    print("6 - Remover vulnerabilidade")
    print("0 - Voltar")

    acao = input("Escolha uma opção: ").strip()

    if acao == "1":
        AtualizarATV(ativo_selecionado)

    elif acao == "2":
        RemoverATV(ativo_selecionado)

    elif acao == "3":
        cadastrar_vulnerabilidade(ativo_selecionado)

    elif acao == "4":
        consultar_vulnerabilidades(ativo_selecionado)

    elif acao == "5":
        atualizar_vulnerabilidade(ativo_selecionado)

    elif acao == "6":
        remover_vulnerabilidade(ativo_selecionado)

    elif acao == "0":
        return

    else:
        print("Opção inválida!")



#atualizar cadastro de ativos
def AtualizarATV(ativo):
    print("\n=== ATUALIZAÇÃO DE ATIVO ===")
    print(f"Equipamento selecionado: {ativo.nome}")

    print("1 - Alterar nome")
    print("2 - Alterar tipo")
    print("3 - Alterar setor")
    print("4 - Alterar responsável")
    print("0 - Cancelar")

    opcao = input("Escolha o campo: ").strip()

    if opcao == "1":
        print(f"Nome atual: {ativo.nome}")
        novo_nome = ler_campo("Digite o novo nome: ")
        ativo.alterar_nome(novo_nome)

    elif opcao == "2":
        print(f"Tipo atual: {ativo.tipo}")
        print("Tipos disponíveis:")
        for categoria in TipoAtivo:
            print(f"{categoria.value} - {categoria.descricao}")
        while True:
            novo_tipo = ler_campo("Código do novo tipo: ")
            try:
                novo_equipamento = criar_equipamento(
                    ativo.id, ativo.nome, novo_tipo, ativo.setor, ativo.responsavel)
                break
            except ValueError:
                print("Tipo inválido! Escolha de 1 a 4.")
        novo_equipamento.vulnerabilidades = ativo.vulnerabilidades
        indice = ativos.index(ativo)
        ativos[indice] = novo_equipamento

    elif opcao == "3":
        print(f"Setor atual: {ativo.setor}")
        novo_setor = ler_campo("Digite o novo setor: ")
        ativo.alterar_setor(novo_setor)

    elif opcao == "4":
        print(f"Responsável atual: {ativo.responsavel}")
        novo_responsavel = ler_campo("Digite o novo responsável: ")
        setattr(ativo, "responsavel", novo_responsavel)

    elif opcao == "0":
        print("Atualização cancelada.")
        return

    else:
        print("Opção inválida!")
        return

    salvar_ativos()
    print("\nAtivo atualizado com sucesso!")




#remover cadastro de ativos
def RemoverATV(ativo):
    print("\n=== REMOVER ATIVO ===")
    print(f"ID: {ativo.id}")
    print(f"Nome: {ativo.nome}")

    confirmacao = input("Deseja realmente remover este ativo? (s/n): ").strip().lower()

    if confirmacao == "s":
        ativos.remove(ativo)
        salvar_ativos()
        print("\nAtivo removido com sucesso!")
    else:
        print("\nRemoção cancelada.")



def selecionar_ativo():
    print("\n=== SELECIONAR ATIVO ===")

    if len(ativos) == 0:
        print("Nenhum ativo cadastrado!")
        return None

    for ativo in ativos:
        print(f"{ativo.id} - {ativo.nome}")

    while True:
        escolha = input(
            "\nDigite o ID do ativo ou 0 para cancelar: "
        ).strip()

        if escolha == "0":
            return None

        for ativo in ativos:
            if str(ativo.id) == escolha:
                return ativo

        print("Ativo não encontrado!")
