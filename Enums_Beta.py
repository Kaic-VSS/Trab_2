from enum import Enum

class Severidade(Enum):
    BAIXA = 'Baixa'
    MEDIA = 'Média'
    ALTA = 'Alta'
    CRITICA = 'Crítica'

class Status(Enum):
    ABERTA = 'Aberta'
    EM_TRATAMENTO = 'Em tratamento'
    CORRIGIDA = 'Corrigida'
    ACEITA = 'Aceita como risco'

class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SOFTWARE = 4

    @property
    def descricao(self):
        return {1: 'Notebook', 2: 'Servidor', 3: 'Roteador', 4: 'Software'}[self.value]

    @classmethod
    def interpretar(cls, valor):
        if isinstance(valor, cls):
            return valor
        texto = str(valor).strip().lower()
        nomes = {'notebook': cls.NOTEBOOK, 'servidor': cls.SERVIDOR,
                 'roteador': cls.ROTEADOR, 'software': cls.SOFTWARE,
                 'software licenciado': cls.SOFTWARE}
        if texto in nomes:
            return nomes[texto]
        if texto.isdigit():
            try:
                return cls(int(texto))
            except ValueError:
                pass
        raise ValueError(f'Tipo de ativo inválido: {valor!r}')

class Equipamento:
    def __init__(self, id, nome, tipo, setor, responsavel):
        self.id = id
        self.nome = nome
        self.tipo = TipoAtivo.interpretar(tipo).descricao.lower()
        self.setor = setor
        self.responsavel = responsavel
        self.vulnerabilidades = []

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_setor(self, novo_setor):
        self.setor = novo_setor

    def descricao_tecnica(self):
        return f'Ativo de TI: {self.nome}'

    def para_dicionario(self):
        return {'id': self.id, 'nome': self.nome, 'tipo': self.tipo,
                'codigo_tipo': TipoAtivo.interpretar(self.tipo).value,
                'classe': type(self).__name__, 'setor': self.setor,
                'responsavel': self.responsavel,
                'vulnerabilidades': self.vulnerabilidades}

    @classmethod
    def de_dicionario(cls, dados):
        equipamento = criar_equipamento(dados['id'], dados['nome'],
            dados.get('codigo_tipo', dados['tipo']), dados['setor'], dados['responsavel'])
        equipamento.vulnerabilidades = dados.get('vulnerabilidades', [])
        return equipamento

class Notebook(Equipamento):
    def descricao_tecnica(self):
        return f'Notebook {self.nome}: equipamento portátil'

class Servidor(Equipamento):
    def descricao_tecnica(self):
        return f'Servidor {self.nome}: fornece serviços à rede'

class Roteador(Equipamento):
    def descricao_tecnica(self):
        return f'Roteador {self.nome}: conecta redes'

class Software(Equipamento):
    def descricao_tecnica(self):
        return f'Software {self.nome}: aplicação ou licença'

def criar_equipamento(id, nome, tipo, setor, responsavel):
    categoria = TipoAtivo.interpretar(tipo)
    classes = {TipoAtivo.NOTEBOOK: Notebook, TipoAtivo.SERVIDOR: Servidor,
               TipoAtivo.ROTEADOR: Roteador, TipoAtivo.SOFTWARE: Software}
    return classes[categoria](id, nome, categoria, setor, responsavel)
