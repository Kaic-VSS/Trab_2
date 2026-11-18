"""Matriz didática de risco: probabilidade x impacto (1 a 5)."""
from Dados_Beta import salvar_ativos
from Vulnerabilidades_Beta import selecionar_vulnerabilidade


def classificar_risco(pontuacao):
    if not 1 <= pontuacao <= 25:
        raise ValueError("Pontuação deve estar entre 1 e 25")
    if pontuacao <= 4:
        return "Baixo"
    if pontuacao <= 9:
        return "Moderado"
    if pontuacao <= 16:
        return "Alto"
    return "Crítico"


def calcular_risco(probabilidade, impacto):
    if type(probabilidade) is not int or type(impacto) is not int:
        raise ValueError("Probabilidade e impacto devem ser inteiros")
    if not (1 <= probabilidade <= 5 and 1 <= impacto <= 5):
        raise ValueError("Probabilidade e impacto devem estar entre 1 e 5")
    pontuacao = probabilidade * impacto
    return {"probabilidade": probabilidade, "impacto": impacto,
            "pontuacao": pontuacao, "nivel": classificar_risco(pontuacao)}


def ler_nota(campo):
    while True:
        entrada = input(f"{campo} (1 a 5, ou 0 para cancelar): ").strip()
        if entrada == "0":
            return None
        if entrada in ("1", "2", "3", "4", "5"):
            return int(entrada)
        print("Digite um número inteiro entre 1 e 5, ou 0 para cancelar.")


def avaliar_risco(ativo):
    print("\n=== ANÁLISE DE RISCO ===")
    vulnerabilidade = selecionar_vulnerabilidade(ativo)
    if vulnerabilidade is None:
        return
    print("Use 1 para menor probabilidade/impacto e 5 para maior.")
    probabilidade = ler_nota("Probabilidade")
    if probabilidade is None:
        print("Avaliação cancelada.")
        return
    impacto = ler_nota("Impacto")
    if impacto is None:
        print("Avaliação cancelada.")
        return
    risco = calcular_risco(probabilidade, impacto)
    vulnerabilidade["risco"] = risco
    salvar_ativos()
    print(f"Risco: {risco['pontuacao']}/25 — {risco['nivel']}")
    print("Avaliação salva no JSON.")
