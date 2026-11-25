# Precificação Preditiva de Imóveis com CRISP-DM

Projeto desenvolvido para a Avaliação A1 da disciplina **Ciência de Dados e Aprendizagem de Máquina** (UDF — Profa. Kadidja Valéria Reginaldo de Oliveira), aplicando integralmente o ciclo de vida **CRISP-DM**.

## Estrutura do Repositório
- `data/raw/` — Bases brutas (`imoveis.csv` e `indicadores_bairros.csv`).
- `data/processed/` — Base limpa, integrada e enriquecida (`imoveis_tratado.csv`).
- `notebooks/01_entendimento_dados.ipynb` — Fase 2: Coleta, descrição, EDA e qualidade.
- `notebooks/02_preparacao_dados.ipynb` — Fase 3: Seleção, limpeza, *feature engineering* e integração.
- `notebooks/03_modelagem_avaliacao.ipynb` — Fases 4 e 5: Modelagem, iteração e avaliação de impacto.
- `docs/01_entendimento_negocio.md` — Fase 1: Objetivos, situação, metas e plano.
- `docs/02_implementacao_monitoramento.md` — Fase 6: Arquitetura, monitoramento e lições aprendidas.
- `docs/relatorio_final_A1.md` — Checklist completo da A1 (28/28 itens documentados).

## Resultados Principais
| Modelo | CV R² (Treino) | R² (Teste) | MAE (R$) | RMSE (R$) | MAPE (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Regressão Linear (Baseline) | 0.8545 | 0.8912 | 131.973,46 | 197.502,55 | 38.38% |
| Random Forest (Padrão) | 0.9216 | 0.9776 | 57.296,18 | 89.688,08 | 9.05% |
| Gradient Boosting (Padrão) | 0.9243 | 0.9742 | 56.678,99 | 96.081,05 | 9.65% |
| **Gradient Boosting (Iteração 2 - Tunado)** | **0.9270** | **0.9779** | **53.752,49** | **88.919,30** | **8.91%** |

## Síntese Final (Os 5 Pilares do CRISP-DM)
1. **Comece pelo Negócio:** O projeto nasceu de uma dor comercial real (perda de vendas/margem por precificação subjetiva), traduzida na meta objetiva de MAPE <= 12%.
2. **Respeite o Atrito:** A maior parcela do esforço concentrou-se na Fase 3 (remoção de dado sensível/CPF, duplicatas, padronização textual, outliers absurdos e imputação).
3. **Abrace a Iteração:** Partimos de um baseline simples (Regressão Linear), comparamos algoritmos de conjunto e realizamos uma 2ª iteração de ajuste de hiperparâmetros no Gradient Boosting, reduzindo o MAE em quase R$ 3.000 e o MAPE para 8,91%.
4. **Mensure o Impacto:** A Regressão Linear atingiu R² = 0,8912, mas falhou no critério de negócio (MAPE de 38,38%). A aprovação do Gradient Boosting Tunado baseou-se no cumprimento da meta comercial (MAPE de 8,91% <= 12%).
5. **Documente a Jornada:** Cada fase possui evidências rastreáveis em código, gráficos e documentação técnica pronta para a equipe de TI.
