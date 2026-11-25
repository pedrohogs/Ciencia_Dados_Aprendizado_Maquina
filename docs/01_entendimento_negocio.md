# Fase 1: Entendimento do Negócio

## 1.1 Objetivos de Negócio e Critérios de Sucesso
- **Cenário:** No mercado imobiliário, a precificação empírica ou subjetiva gera dois prejuízos diretos: imóveis anunciados acima do valor de mercado ficam encalhados (aumentando o custo de oportunidade e tempo de venda), enquanto imóveis subavaliados geram perda financeira para o proprietário e redução na comissão da imobiliária.
- **Objetivo de Negócio:** Desenvolver um modelo preditivo capaz de estimar o valor justo de venda de imóveis residenciais a partir de suas características físicas e indicadores socioeconômicos do bairro.
- **Critério de Sucesso de Negócio:** Atingir uma margem de erro percentual média (MAPE) de **no máximo 12%** em relação ao valor real de venda, garantindo agilidade e padronização na captação de imóveis.

## 1.2 Avaliação da Situação
- **Recursos Disponíveis:** Ambiente Python (VS Code / Google Colab), bibliotecas open-source (`pandas`, `scikit-learn`, `seaborn`, `matplotlib`) e duas bases de dados: registros de anúncios imobiliários (`imoveis.csv`) e indicadores regionais por bairro (`indicadores_bairros.csv`).
- **Riscos e Premissas:** Bases de anúncios frequentemente contêm erros de digitação (outliers de área ou preço), registros duplicados e campos ausentes (como vagas de garagem ou condomínio). Assume-se que os preços históricos refletem o comportamento recente do mercado.
- **Análise de Custo-Benefício:** Custo financeiro de infraestrutura próximo de zero (ferramentas gratuitas) frente ao alto retorno comercial na assertividade das avaliações.

## 1.3 Metas Técnicas de Mineração de Dados
- **Abordagem:** Aprendizado de Máquina Supervisionado — **Regressão**.
- **Algoritmos Candidatos:** Regressão Linear (baseline), Random Forest Regressor e Gradient Boosting Regressor.
- **Critérios Técnicos de Sucesso:**
  - Coeficiente de Determinação ($R^2$) $\ge 0.80$ no conjunto de teste.
  - Minimização do **MAE** (Erro Absoluto Médio em R$) e **RMSE** (Raiz do Erro Quadrático Médio).

## 1.4 Plano de Projeto
O projeto segue o ciclo iterativo do modelo **CRISP-DM**, com maior alocação de esforço na preparação dos dados:
1. **Entendimento do Negócio (10%):** Definição de metas e critérios de sucesso.
2. **Entendimento dos Dados (15%):** Coleta, EDA (análise exploratória) e relatório de qualidade.
3. **Preparação dos Dados (50%):** Limpeza de outliers/nulos, *feature engineering* e integração das bases.
4. **Modelagem (10%):** Treino/teste, comparação de algoritmos e ajuste de hiperparâmetros.
5. **Avaliação (10%):** Confronto das métricas técnicas com a meta de negócio (MAPE $\le 12\%$).
6. **Implementação (5%):** Documentação da arquitetura, plano de monitoramento e relatório final.
```[cite: 4, 6, 14, 15]

---

### 3. Gere a base de dados bruta (`data/raw/`)
Para termos **duas tabelas reais** (necessário para o item **3.4 Integração**) e **problemas realistas de qualidade** (necessário para os itens **2.4** e **3.2**, como nulos, duplicatas e erros de digitação), crie um arquivo temporário `gerar_dados.py` na raiz do projeto, cole o código abaixo e execute no terminal com `python gerar_dados.py`:

```python
import numpy as np
import pandas as pd

np.random.seed(42)
n = 1200

# 1. Tabela de Indicadores por Bairro (para integração na Fase 3)
bairros_info = pd.DataFrame({
    "bairro": ["Asa Sul", "Asa Norte", "Águas Claras", "Guará", "Taguatinga", "Samambaia", "Planaltina", "Sobradinho"],
    "renda_media_bairro": [12500, 11800, 8200, 6500, 4800, 3200, 2900, 5400],
    "indice_infraestrutura": [9.4, 9.2, 8.5, 7.8, 7