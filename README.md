# Projeto de Ciência de Dados

Este repositório é dedicado ao treinamento de diversos exercícios de Ciência de Dados, utilizando o gerenciador de pacotes `uv` para um ambiente Python rápido e moderno.

## Estrutura do Projeto

A organização do projeto segue uma estrutura modular para facilitar o aprendizado e a expansão:

- `data/`: Contém os bancos de dados, arquivos CSV e outros datasets utilizados nos exercícios.
- `exercicios/`: Pasta principal organizada por tópicos. Cada subpasta contém um exercício específico.
    - `01_pandas_sqlite/`: Introdução à manipulação de dados com Pandas e integração com SQLite.
- `notebooks/`: Arquivos Jupyter Notebook (`.ipynb`) para exploração interativa.
- `pyproject.toml`: Configuração do projeto e dependências (gerenciado pelo `uv`).

## Como Instalar

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd projeto_ciencia_dados
```

2. Instale as dependências:
```bash
uv sync
```

## Como Executar um Exercício

Para executar um exercício específico (ex: Exercício 01):

```bash
uv run exercicios/01_pandas_sqlite/main.py
```

## Dependências Principais

- Pandas
- SQLAlchemy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter
