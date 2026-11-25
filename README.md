**Profa. Kadidja Valéria | UDF · Ciência de Dados e Aprendizagem de Máquina · Ciência da Computação · 2026.2**

# Projeto CRISP-DM — Precificação Preditiva de Imóveis Residenciais no DF

**Equipe:** Pedro Henrique de Oliveira Gomes · **Conclusão das 6 fases:** 25/11/2026 · **Metodologia:** CRISP-DM · **Checklist A1:** [relatorio_final_A1.md](docs/relatorio_final_A1.md)

---

**Pergunta:** Quais fatores físicos e socioeconômicos mais influenciam o preço de venda de imóveis residenciais no Distrito Federal, e é possível automatizar a precificação com erro médio inferior a 12%?

**Resposta curta:**
* **Base usada:** conjunto de demonstração realista do mercado imobiliário do DF, com **1.215 registros brutos** (após limpeza: base tratada e integrada com indicadores de **8 regiões/bairros**).
* **Modelo vencedor:** **Gradient Boosting Regressor (Iteração 2 — Tunado)** atingiu **$R^2 = 0,9779$** no conjunto de teste e **MAE de R$ 53.752,49**.
* **Impacto no negócio:** erro percentual médio (**MAPE**) de **8,91%**, superando a meta comercial definida na Fase 1 ($\le 12\%$) e provando na prática que *Impacto Real > Precisão Técnica* (a Regressão Linear atingiu $R^2 = 0,8912$, mas falhou no negócio com MAPE de **38,38%**).
* **Decisão:** **Aprovado para implementação (Fase 6)** via API REST com monitoramento trimestral de *drift*.

---

## Comparativo de Modelos (Fase 4 e Fase 5)

| Modelo | CV R² (Treino) | R² (Teste) | MAE (R$) | RMSE (R$) | MAPE (%) | Meta de Negócio (<= 12%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Regressão Linear (Baseline) | 0.8545 | 0.8912 | 131.973,46 | 197.502,55 | 38.38% | Reprovado |
| Random Forest (Padrão) | 0.9216 | 0.9776 | 57.296,18 | 89.688,08 | 9.05% | Aprovado |
| Gradient Boosting (Padrão) | 0.9243 | 0.9742 | 56.678,99 | 96.081,05 | 9.65% | Aprovado |
| **Gradient Boosting (Iteração 2 - Tunado)** | **0.9270** | **0.9779** | **53.752,49** | **88.919,30** | **8.91%** | **Aprovado (Vencedor)** |

---

## Navegação pelo Ciclo CRISP-DM (Evidências Rastreáveis)

* **Fase 1 — Entendimento do Negócio:** [docs/01_entendimento_negocio.md](docs/01_entendimento_negocio.md)
* **Fase 2 — Entendimento dos Dados:** [notebooks/01_entendimento_dados.ipynb](notebooks/01_entendimento_dados.ipynb) | Bases brutas: [data/raw/](data/raw/)
* **Fase 3 — Preparação dos Dados:** [notebooks/02_preparacao_dados.ipynb](notebooks/02_preparacao_dados.ipynb) | Base tratada: [data/processed/imoveis_tratado.csv](data/processed/imoveis_tratado.csv)
* **Fases 4 e 5 — Modelagem e Avaliação:** [notebooks/03_modelagem_avaliacao.ipynb](notebooks/03_modelagem_avaliacao.ipynb)
* **Fase 6 — Implementação e Monitoramento:** [docs/02_implementacao_monitoramento.md](docs/02_implementacao_monitoramento.md)
* **Relatório Completo A1 (28/28 itens):** [docs/relatorio_final_A1.md](docs/relatorio_final_A1.md)

---

## Síntese Final (Os 5 Pilares do CRISP-DM)
1. **Comece pelo Negócio:** O projeto nasceu de uma dor comercial real (perda de vendas e margem por precificação subjetiva), traduzida na meta objetiva de MAPE <= 12%.
2. **Respeite o Atrito:** A maior parcela do esforço concentrou-se na Fase 3 (remoção de dado sensível/CPF, duplicatas, padronização textual, outliers absurdos e imputação).
3. **Abrace a Iteração:** Partimos de um baseline simples (Regressão Linear), comparamos algoritmos de conjunto e realizamos uma 2ª iteração de ajuste de hiperparâmetros no Gradient Boosting, reduzindo o MAPE para 8,91%.
4. **Mensure o Impacto:** A Regressão Linear atingiu R² = 0,8912, mas falhou no critério comercial (MAPE de 38,38%). A aprovação do modelo final baseou-se no impacto real para o negócio.
5. **Documente a Jornada:** Cada fase possui evidências rastreáveis em código, gráficos e documentação técnica pronta para a equipe de TI.
