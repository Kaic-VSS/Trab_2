from enum import Enum


# Severidade das vulnerabilidades
class Severidade(Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"
    CRITICA = "Crítica"


# Status de tratamento
class Status(Enum):
    ABERTA = "Aberta"
    EM_TRATAMENTO = "Em tratamento"
    CORRIGIDA = "Corrigida"
    ACEITA = "Aceita como risco"


# Classe dos equipamentos
class Equipamento:

    # Inicializar equipamento
    def __init__(self, id, nome, tipo, setor, responsavel):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.setor = setor
        self.responsavel = responsavel
        self.vulnerabilidades = []

    # Alterar nome do equipamento
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    # Alterar setor do equipamento
    def alterar_setor(self, novo_setor):
        self.setor = novo_setor

    # Converter objeto em dicionário
    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "setor": self.setor,
            "responsavel": self.responsavel,
            "vulnerabilidades": self.vulnerabilidades
        }

    # Converter dicionário em objeto
    @classmethod
    def de_dicionario(cls, dados):
        equipamento = cls(
            dados["id"],
            dados["nome"],
            dados["tipo"],
            dados["setor"],
            dados["responsavel"]
        )

        equipamento.vulnerabilidades = dados.get("vulnerabilidades", [])

        return equipamento