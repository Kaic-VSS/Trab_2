import json
import os
from pathlib import Path
from Enums_Beta import Equipamento


caminho_json = Path(os.environ.get("ATIVOS_JSON", str(Path(__file__).parent / "ativos.json")))
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

    caminho_json.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
