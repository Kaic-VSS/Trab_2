
from enum import Enum

class Severidade(Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"
    CRITICA = "Crítica"


class Status(Enum):
    ABERTA = "Aberta"
    EM_TRATAMENTO = "Em tratamento"
    CORRIGIDA = "Corrigida"
    ACEITA = "Aceita como risco"



class Equipamento:
    def __init__(self, id, nome, tipo, setor, responsavel):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.setor = setor
        self.responsavel = responsavel
        self.vulnerabilidades = []
