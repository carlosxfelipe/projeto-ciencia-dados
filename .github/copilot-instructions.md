# AI Instructions & Skills: Python UV Standard

Este documento contém instruções de comportamento e habilidades obrigatórias para assistentes de IA (como Antigravity e GitHub Copilot) que trabalharem neste repositório.

## Gerenciamento de Projeto com `uv`

Este projeto utiliza estritamente o `uv`. Siga estas regras:

1. **Dependências**:
    - Sempre use `uv add <pacote>` para instalar.
    - Sempre use `uv remove <pacote>` para desinstalar.
    - NUNCA use `pip`.

2. **Execução de Código**:
    - Sempre use `uv run <comando>` para garantir que o ambiente virtual está correto.
    - Exemplos: `uv run python main.py`, `uv run jupyter notebook`.

3. **Ambiente Virtual**:
    - O ambiente está em `.venv`. Não tente criar outros com `python -m venv`.

4. **Sincronização**:
    - Se houver mudanças no `pyproject.toml`, execute `uv sync`.

## Formatação de Imports (Ruff)

Os imports devem seguir o padrão determinado pelo **Ruff** (I001):

1. **Ordem**:
    - Bibliotecas padrão do Python (Standard Library) primeiro (ex: `import os`).
    - Bibliotecas de terceiros (Third-party) em seguida (ex: `import pandas as pd`).
    - Imports locais do projeto por último.
2. **Estilo**:
    - Use linhas em branco para separar os grupos acima.
    - Ordene alfabeticamente dentro de cada grupo.
    - **NUNCA** coloque múltiplos imports na mesma linha.
      *   Certo:
          ```python
          import os
          import sys
          ```
      *   Errado: `import os, sys`
    - **NUNCA** deixe imports não utilizados no código.
    - **PREFIRA** imports absolutos em vez de relativos para maior clareza.

Exemplo Correto:
```python
import os
import sys

import pandas as pd
from sqlalchemy import create_engine

from meu_projeto.modulo import minha_funcao
```

💡 **Dicas de Automação**:
- Use `uv run ruff check --fix` para corrigir automaticamente problemas de ordenação e excesso de imports.
- Use `uv run ruff format` para padronizar todo o código do projeto.

## Tom de Voz e Estilo
- Garanta que as soluções sejam modernas e sigam as melhores práticas de Ciência de Dados com Python 3.12+.
