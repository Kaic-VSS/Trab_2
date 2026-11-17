import json
from pathlib import Path
from Enums_Beta import Equipamento


caminho_json = Path(__file__).parent / "ativos.json"
#Carregar ativos para procurar
def carregar_ativos():
    if not caminho_json.exists():
        return []

    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    equipamentos = []

    for dado in dados:
        equipamento = Equipamento.de_dicionario(dado)
        equipamentos.append(equipamento)

    return equipamentos


ativos = carregar_ativos()

#salvar ativos atualizados no arquivo JSON
def salvar_ativos():
    dados = []

    for equipamento in ativos:
        dados.append(equipamento.para_dicionario())

    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)



def migrar_vulnerabilidades():
    alterado = False

    for ativo in ativos:
        if "vulnerabilidade" not in ativo:
            continue

        descricao = ativo["vulnerabilidade"].strip()

        if "vulnerabilidades" not in ativo:
            ativo["vulnerabilidades"] = []

        if descricao:
            nova_vulnerabilidade = {
                "descricao": descricao,
                "categoria": "Não informada",
                "severidade": "Não classificada",
                "status": "Não informado"
            }

            ativo["vulnerabilidades"].append(nova_vulnerabilidade)

        del ativo["vulnerabilidade"]
        alterado = True

    if alterado:
        salvar_ativos()
        print("Migração concluída com sucesso!")
    else:
        print("Nenhuma migração necessária.")
