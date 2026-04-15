import os
import pandas as pd
from sqlalchemy import create_engine, text

# 1. Criar dados de exemplo
dados = pd.DataFrame(
    {
        "aluno": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
        "nota_final": [9.5, 7.0, 8.5, 6.0, 9.0],
        "horas_estudo": [20, 15, 18, 10, 22],
    }
)


# Definir caminhos relativos ao projeto
# __file__ é o caminho deste arquivo main.py.
# abspath(__file__) garante o caminho completo, e dirname() pega a pasta onde este arquivo está.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Como este arquivo está em 'exercicios/01_pandas_sqlite/', precisamos subir dois níveis ("../../")
# para chegar na raiz do projeto e então entrar na pasta 'data/'.
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../data"))

# Define o caminho completo para o arquivo do banco de dados
DB_PATH = os.path.join(DATA_DIR, "escola.db")

# Garantir que a pasta data exista
os.makedirs(DATA_DIR, exist_ok=True)

# 2. Criar conexão com SQLite
engine = create_engine(f"sqlite:///{DB_PATH}")

# 3. Salvar o DataFrame no Banco de Dados
print(f"Salvando dados no banco {DB_PATH}...")
dados.to_sql("notas", con=engine, if_exists="replace", index=False)

# 4. Ler do Banco de Dados usando SQL
# (Usamos um gerenciador de contexto 'with' para garantir que a conexão seja fechada)
query = text("SELECT * FROM notas WHERE nota_final >= 8")

with engine.connect() as conn:
    df_do_banco = pd.read_sql(query, con=conn)

print("\n--- Relatório Final ---")
print("Alunos com nota acima ou igual a 8:")
print(df_do_banco)
print("\nProjeto configurado com sucesso!")
