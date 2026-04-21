# Projeto de Ciência de Dados

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este repositório é dedicado ao treinamento e desenvolvimento de habilidades em Ciência de Dados. Utilizamos o ecossistema moderno do Python, com foco em performance e reprodutibilidade através do gerenciador de pacotes `uv`.

---

## Tecnologias Principais

O projeto utiliza o que há de mais moderno no ecossistema de dados:

-   **[Pandas](https://pandas.pydata.org/)**: Manipulação e análise de dados de alta performance.
-   **[Scikit-Learn](https://scikit-learn.org/)**: Ferramentas simples e eficientes para análise preditiva de dados.
-   **[SQLAlchemy](https://www.sqlalchemy.org/)**: O Toolkit SQL para Python e Object Relational Mapper.
-   **[Matplotlib](https://matplotlib.org/)** & **[Seaborn](https://seaborn.pydata.org/)**: Visualização de dados estática, animada e interativa.
-   **[Jupyter](https://jupyter.org/)**: Ambiente computacional interativo para criação de documentos.

---

## Estrutura do Projeto

A organização segue uma abordagem modular e intuitiva:

```text
.
├── exercicios/          # Treinamentos práticos organizados por temas
│   └── 01_pandas_sqlite/ # Manipulação de CSV e integração com SQLite
├── notebooks/           # Jupyter Notebooks para exploração e prototipagem
├── main.py              # Ponto de entrada principal (opcional)
├── pyproject.toml       # Definições de dependências e metadados (UV)
└── uv.lock              # Lockfile para garantir reprodutibilidade
```

---

## Como Começar

Este projeto utiliza o [uv](https://github.com/astral-sh/uv) para gerenciamento de ambiente.

### 1. Requisitos

Certifique-se de ter o `uv` instalado em sua máquina:

**Linux / macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Instalação

Clone o repositório e instale as dependências automaticamente:

```bash
git clone https://github.com/carlosxfelipe/projeto-ciencia-dados.git
cd projeto-ciencia-dados
uv sync
```

### 3. Executando um Exercício

Para rodar o script de um exercício específico de forma isolada:

```bash
uv run exercicios/01_pandas_sqlite/main.py
```

### 4. Abrindo o Jupyter Lab

Para exploração visual nos arquivos do diretório `notebooks`:

```bash
uv run jupyter lab
```

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
