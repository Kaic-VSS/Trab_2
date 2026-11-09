import json
from pathlib import Path

caminho_json = Path(__file__).parent / "ativos.json"
#Carregar ativos para procurar
def carregar_ativos():
    if not caminho_json.exists():
        return []

    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


ativos = carregar_ativos()

#salvar ativos atualizados no arquivo JSON
def salvar_ativos():
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(ativos, arquivo, indent=4, ensure_ascii=False)
