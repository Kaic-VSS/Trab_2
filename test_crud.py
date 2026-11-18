import json
import pytest
from Enums_Beta import Equipamento, Notebook, Servidor, Roteador, Software, TipoAtivo, criar_equipamento
import Dados_Beta as dados
import Ativos_Beta as cadastro
import Vulnerabilidades_Beta as vulns
from Riscos_Beta import calcular_risco, classificar_risco, avaliar_risco

@pytest.fixture
def isolado(tmp_path, monkeypatch):
    monkeypatch.setattr(dados, "caminho_json", tmp_path / "ativos.json")
    dados.ativos.clear()
    yield dados
    dados.ativos.clear()

def test_subclasses_enum_e_polimorfismo():
    for codigo, classe in [(1, Notebook), (2, Servidor), (3, Roteador), (4, Software)]:
        ativo = criar_equipamento(codigo, "Teste", codigo, "TI", "Ana")
        assert isinstance(ativo, classe)
        assert ativo.tipo == TipoAtivo(codigo).descricao.lower()
        assert ativo.descricao_tecnica() != Equipamento.descricao_tecnica(ativo)

@pytest.mark.parametrize("p,i,esperado", [(1,1,"Baixo"),(2,3,"Moderado"),(4,4,"Alto"),(5,5,"Crítico")])
def test_faixas_risco(p, i, esperado):
    assert calcular_risco(p,i)["nivel"] == esperado
    assert calcular_risco(p,i)["pontuacao"] == p*i

@pytest.mark.parametrize("p,i", [(0,2),(6,2),(1,9),(True,2),(1.5,2)])
def test_risco_invalido(p,i):
    with pytest.raises(ValueError): calcular_risco(p,i)

def test_salvar_e_recarregar_objetos(isolado):
    a = criar_equipamento(1, "Servidor A", 2, "TI", "Ana")
    a.vulnerabilidades.append({"descricao":"Falha","categoria":"Rede","severidade":"Alta","status":"Aberta","risco":calcular_risco(4,5)})
    isolado.ativos.append(a)
    isolado.salvar_ativos()
    assert json.loads(isolado.caminho_json.read_text(encoding="utf-8"))[0]["id"] == 1
    b = isolado.carregar_ativos()[0]
    assert isinstance(b, Servidor)
    assert b.vulnerabilidades[0]["risco"]["pontuacao"] == 20

def test_cadastro_e_id_unico(isolado, monkeypatch):
    entradas=iter(["1","Notebook A","1","TI","Ana","Falha","Rede","1","1","n"])
    monkeypatch.setattr("builtins.input",lambda _:next(entradas))
    cadastro.cadastro_ativo()
    assert len(isolado.ativos)==1
    assert len(isolado.carregar_ativos()[0].vulnerabilidades)==1
    entradas=iter(["1","2","Servidor B","2","TI","Bia","Falha 2","Rede","2","1","n"])
    monkeypatch.setattr("builtins.input",lambda _:next(entradas))
    cadastro.cadastro_ativo()
    assert [a.id for a in isolado.ativos]==[1,2]

def test_consultar_atualizar_remover_ativo(isolado, monkeypatch, capsys):
    a=criar_equipamento(1,"A",1,"TI","Ana")
    isolado.ativos.append(a)
    entradas=iter(["1","1","0"])
    monkeypatch.setattr("builtins.input",lambda _:next(entradas))
    cadastro.ConsultarATV()
    assert "Notebook" in capsys.readouterr().out
    entradas=iter(["1","Novo nome"])
    monkeypatch.setattr("builtins.input",lambda _:next(entradas))
    cadastro.AtualizarATV(a)
    assert isolado.carregar_ativos()[0].nome=="Novo nome"
    monkeypatch.setattr("builtins.input",lambda _:"s")
    cadastro.RemoverATV(a)
    assert isolado.carregar_ativos()==[]

def test_vulnerabilidade_atualizar_remover(isolado, monkeypatch):
    a=criar_equipamento(1,"A",1,"TI","Ana")
    a.vulnerabilidades=[{"descricao":"Antiga","categoria":"Rede","severidade":"Alta","status":"Aberta"}]
    isolado.ativos.append(a)
    entradas=iter(["1","1","Nova"])
    monkeypatch.setattr("builtins.input",lambda _:next(entradas))
    vulns.atualizar_vulnerabilidade(a)
    assert isolado.carregar_ativos()[0].vulnerabilidades[0]["descricao"]=="Nova"
    entradas=iter(["1","s"])
    monkeypatch.setattr("builtins.input",lambda _:next(entradas))
    vulns.remover_vulnerabilidade(a)
    assert isolado.carregar_ativos()[0].vulnerabilidades==[]

def test_avaliar_risco_persiste(isolado, monkeypatch):
    a=criar_equipamento(1,"A",1,"TI","Ana")
    a.vulnerabilidades=[{"descricao":"Falha","categoria":"Rede","severidade":"Alta","status":"Aberta"}]
    isolado.ativos.append(a)
    entradas=iter(["1","4","5"])
    monkeypatch.setattr("builtins.input",lambda _:next(entradas))
    avaliar_risco(a)
    assert isolado.carregar_ativos()[0].vulnerabilidades[0]["risco"]["nivel"]=="Crítico"
