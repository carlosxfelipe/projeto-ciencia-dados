import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Configurar o estilo visual
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


def gerar_dados_vendas():
    """Gera dados sintéticos de vendas com tendência e ruído."""
    # Semente para reprodutibilidade
    np.random.seed(42)

    # Dias do mês
    dias = np.arange(1, 31)

    # Tendência de crescimento linear + ruído aleatório
    tendencia = 100 + (dias * 5)
    ruido = np.random.normal(0, 15, size=dias.shape)
    vendas = tendencia + ruido

    return dias, vendas


def main():
    print("Iniciando Exercício 02: Simulação e Visualização...")

    # Gerar dados usando NumPy
    dias, vendas = gerar_dados_vendas()

    # 2. Criar a visualização
    plt.figure()
    sns.lineplot(x=dias, y=vendas, marker="o", label="Vendas Diárias")
    sns.regplot(x=dias, y=vendas, scatter=False, color="red", label="Tendência (Regressão)")

    plt.title("Tendência de Vendas Mensais - Simulação NumPy", fontsize=16)
    plt.xlabel("Dia do Mês", fontsize=12)
    plt.ylabel("Valor em Reais (R$)", fontsize=12)
    plt.legend()

    # 3. Definir caminhos e salvar
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../data"))
    os.makedirs(DATA_DIR, exist_ok=True)

    OUTPUT_FILE = os.path.join(DATA_DIR, "tendencia_vendas.png")

    print(f"Salvando gráfico em: {OUTPUT_FILE}")
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
    plt.close()

    print("\n--- Relatório Estatístico ---")
    print(f"Média de Vendas: R$ {np.mean(vendas):.2f}")
    print(f"Desvio Padrão: R$ {np.std(vendas):.2f}")
    print(f"Venda Máxima: R$ {np.max(vendas):.2f} (Dia {dias[np.argmax(vendas)]})")
    print("\nExercício 02 concluído com sucesso!")


if __name__ == "__main__":
    main()
