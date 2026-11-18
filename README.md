# CRUD de ativos e vulnerabilidades — POO

Projeto acadêmico em Python: cadastro, consulta, atualização e remoção de ativos e vulnerabilidades, com persistência JSON, tipos via Enum, herança, polimorfismo e matriz didática de risco.

## Execução local

Requer Python 3.10+. Na pasta do projeto:

```bash
python Menus_Alpha.py
```

O arquivo `ativos.json` começa vazio (`[]`). **Faça backup do seu JSON antes de substituir arquivos.** O caminho pode ser configurado com a variável de ambiente `ATIVOS_JSON`.

## Testes

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q --cov=. --cov-report=term-missing
```

Testes usam `tmp_path`, sem modificar `ativos.json` real. CI em `.github/workflows/testes.yml` executa testes após push ou pull request.

## Docker

```bash
docker compose build
docker compose run --rm crud
```

O volume `dados_ativos` preserva `ativos.json` entre execuções. **Este projeto é um aplicativo de terminal**, não um servidor HTTP; `docker compose up -d` não cria serviço de rede nem comprova disponibilidade por 24h. Para um requisito de API/servidor 24h será necessário implementar um serviço e realizar implantação real.

## Estrutura

- `Enums_Beta.py`: Enum, classe base e subclasses.
- `Dados_Beta.py`: leitura e gravação de JSON.
- `Ativos_Beta.py`: CRUD de ativos.
- `Vulnerabilidades_Beta.py`: CRUD de vulnerabilidades.
- `Riscos_Beta.py`: matriz probabilidade × impacto, de 1 a 5.
- `Validacoes_Beta.py`: validação de entradas.
- `Menus_Alpha.py`: interface de terminal.
- `tests/test_crud.py`: testes automatizados.

## Risco

Pontuação = probabilidade × impacto (ambos de 1 a 5). Faixas didáticas: 1–4 Baixo, 5–9 Moderado, 10–16 Alto, 17–25 Crítico. Não é CVSS e não substitui avaliação profissional.

## Limites e pendências de entrega

- Não há API REST, serviço HTTP, implantação 24h nem prova de uptime.
- A cobertura automatizada não representa validação de todas as entradas e fluxos interativos.
- Histórico de commits, branches e merges deve ser realizado e demonstrado no repositório real.
- Requisitos adicionais do enunciado final devem ser conferidos separadamente.
