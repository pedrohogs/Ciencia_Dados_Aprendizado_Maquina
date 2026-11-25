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
1. **Comece pelo Negócio:** O projeto nasceu de uma dor comercial real (perda de vendas/margem por precificação subjetiva), traduzida na meta objetiva de MAPE $\le 12\%$.
2. **Respeite o Atrito:** A maior parcela do esforço concentrou-se na Fase 3 (remoção de dado sensível/CPF, duplicatas, padronização textual, outliers absurdos e imputação).
3. **Abrace a Iteração:** Partimos de um baseline simples (Regressão Linear), comparamos algoritmos de conjunto e realizamos uma 2ª iteração de ajuste de hiperparâmetros no Gradient Boosting, reduzindo o MAE em quase R$ 3.000 e o MAPE para 8,91%.
4. **Mensure o Impacto:** A Regressão Linear atingiu $R^2 = 0,8912$, mas falhou no critério de negócio (MAPE de 38,38%). A aprovação do Gradient Boosting Tunado baseou-se no cumprimento da meta comercial (MAPE de 8,91% $\le$ 12%).
5. **Documente a Jornada:** Cada fase possui evidências rastreáveis em código, gráficos e documentação técnica pronta para a equipe de TI.
```[cite: 25]

---

#### 3. Abra `docs/relatorio_final_A1.md`, cole, preencha apenas o cabeçalho (Curso, Turma, Turno, RGM) e salve (`Ctrl + S`):

```markdown
# Relatório de Entrega — Avaliação A1 (Checklist CRISP-DM)

- **Projeto:** Precificação Preditiva de Imóveis Residenciais com CRISP-DM
- **Disciplina:** Ciência de Dados e Aprendizagem de Máquina — Profa. Kadidja Valéria Reginaldo de Oliveira
- **Curso:** Ciência da Computação
- **Turma / Turno:** [PREENCHER]
- **Data da Avaliação A1:** 25/11/2026
- **Repositório:** https://github.com/pedrohogs/Ciencia_Dados_Aprendizado_Maquina
- **Integrante:** Pedro Henrique de Oliveira Gomes | **R.G.M.:** [PREENCHER] | **Contribuição:** Desenvolvimento integral (Fases 1 a 6)
- **Resumo:** 28 de 28 itens documentados | 28 realizados | 0 parciais | 0 não realizados

---

## Fase 1 — Entendimento do Negócio
- **1.1 Objetivos de negócio e critérios de sucesso** — *Realizado*
  - **Descrição:** Estimar o preço justo de venda de imóveis residenciais visando reduzir o erro de precificação para MAPE $\le 12\%$.
  - **Evidência:** `docs/01_entendimento_negocio.md` (seção 1.1).
- **1.2 Avaliação da situação** — *Realizado*
  - **Descrição:** Mapeamento de recursos (Python/open-source), riscos (outliers, nulos, duplicatas) e análise de custo-benefício.
  - **Evidência:** `docs/01_entendimento_negocio.md` (seção 1.2).
- **1.3 Metas técnicas de mineração de dados** — *Realizado*
  - **Descrição:** Problema de Regressão Supervisionada com meta técnica de $R^2 \ge 0,80$ e minimização de MAE e RMSE.
  - **Evidência:** `docs/01_entendimento_negocio.md` (seção 1.3).
- **1.4 Plano de projeto** — *Realizado*
  - **Descrição:** Cronograma nas 6 fases do CRISP-DM alocando 50% do esforço à Fase 3 (Preparação dos Dados).
  - **Evidência:** `docs/01_entendimento_negocio.md` (seção 1.4).

## Fase 2 — Entendimento dos Dados
- **2.1 Coleta inicial** — *Realizado*
  - **Descrição:** Obtenção de duas bases: `imoveis.csv` (1.215 registros brutos, 11 colunas) e `indicadores_bairros.csv` (8 bairros, 4 colunas).
  - **Evidência:** `data/raw/` e `notebooks/01_entendimento_dados.ipynb` (seção 2.1).
- **2.2 Descrição dos dados** — *Realizado*
  - **Descrição:** Levantamento de tipos de dados, volumes e estatísticas descritivas (`info()` e `describe()`).
  - **Evidência:** `notebooks/01_entendimento_dados.ipynb` (seção 2.2).
- **2.3 Exploração dos dados** — *Realizado*
  - **Descrição:** Análise exploratória com 3 gráficos (distribuição de preços, dispersão área vs. preço por tipo e preço médio por bairro).
  - **Evidência:** `notebooks/01_entendimento_dados.ipynb` (seção 2.3).
- **2.4 Verificação da qualidade** — *Realizado*
  - **Descrição:** Detecção de valores nulos (`vagas_garagem`, `condominio`, `idade_imovel`), 15 duplicatas, inconsistência textual (`"asa sul"`), outliers extremos (área 0 m², preço R$ 1,00, 45 quartos) e dado sensível (`cpf_proprietario`).
  - **Evidência:** `notebooks/01_entendimento_dados.ipynb` (seção 2.4).

## Fase 3 — Preparação dos Dados
- **3.1 Seleção** — *Realizado*
  - **Descrição:** Remoção do atributo sensível `cpf_proprietario` (LGPD) e do identificador `id_imovel`.
  - **Evidência:** `notebooks/02_preparacao_dados.ipynb` (seção 3.1).
- **3.2 Limpeza** — *Realizado*
  - **Descrição:** Remoção de duplicatas e outliers absurdos, padronização de texto em `bairro` e imputação pela mediana (geral e agrupada por tipo).
  - **Evidência:** `notebooks/02_preparacao_dados.ipynb` (seção 3.2).
- **3.3 Construção** — *Realizado*
  - **Descrição:** Criação dos atributos derivados `area_por_quarto`, `total_comodos` e `relacao_condominio_m2`.
  - **Evidência:** `notebooks/02_preparacao_dados.ipynb` (seção 3.3).
- **3.4 Integração** — *Realizado*
  - **Descrição:** Mesclagem (*left join*) de `imoveis.csv` com `indicadores_bairros.csv` pela chave `bairro`, gerando `data/processed/imoveis_tratado.csv`.
  - **Evidência:** `notebooks/02_preparacao_dados.ipynb` (seção 3.4) e `data/processed/imoveis_tratado.csv`.

## Fase 4 — Modelagem
- **4.1 Seleção de técnicas** — *Realizado*
  - **Descrição:** Seleção e comparação de 3 algoritmos de regressão: Regressão Linear (baseline), Random Forest e Gradient Boosting.
  - **Evidência:** `notebooks/03_modelagem_avaliacao.ipynb` (seção 4.1).
- **4.2 Construção e iteração** — *Realizado*
  - **Descrição:** Execução da Iteração 1 (modelos padrão) seguida pela Iteração 2 com ajuste de hiperparâmetros no Gradient Boosting (`n_estimators=250`, `learning_rate=0.05`, `max_depth=4`), reduzindo o MAPE de 9,65% para 8,91%.
  - **Evidência:** `notebooks/03_modelagem_avaliacao.ipynb` (seção 4.2).
- **4.3 Design de teste** — *Realizado*
  - **Descrição:** Partição estratificada/aleatória em 80% treino / 20% teste (`random_state=42`) combinada com validação cruzada 5-Fold no treino.
  - **Evidência:** `notebooks/03_modelagem_avaliacao.ipynb` (seção 4.3).
- **4.4 Avaliação técnica estatística** — *Realizado*
  - **Descrição:** Avaliação comparativa via CV $R^2$, $R^2$ de teste, MAE, RMSE e MAPE. Melhor modelo: Gradient Boosting Tunado ($R^2 = 0,9779$, MAE = R$ 53.752,49, RMSE = R$ 88.919,30, MAPE = 8,91%).
  - **Evidência:** `notebooks/03_modelagem_avaliacao.ipynb` (seção 4.4).

## Fase 5 — Avaliação
- **5.1 Resultados frente às metas** — *Realizado*
  - **Descrição:** Confronto direto com a Fase 1: meta técnica ($R^2 \ge 0,80$) superada com $0,9779$; meta de negócio (MAPE $\le 12\%$) superada com $8,91\%$. A Regressão Linear atingiu $R^2 = 0,8912$, mas falhou no negócio (MAPE $38,38\%$).
  - **Evidência:** `notebooks/03_modelagem_avaliacao.ipynb` (seção 5.1).
- **5.2 Revisão de falhas** — *Realizado*
  - **Descrição:** Análise de erro percentual por tipo de imóvel, gráfico Real vs. Previsto e ranking de importância das variáveis.
  - **Evidência:** `notebooks/03_modelagem_avaliacao.ipynb` (seção 5.2).
- **5.3 Decisão: implementar ou iterar** — *Realizado*
  - **Descrição:** Decisão formal de **Aprovar para Implementação (Fase 6)**, pois o modelo cumpriu ambos os critérios (técnico e comercial).
  - **Evidência:** `notebooks/03_modelagem_avaliacao.ipynb` (seção 5.3).

## Fase 6 — Implementação
- **6.1 Plano de implementação** — *Realizado*
  - **Descrição:** Arquitetura baseada em serialização do modelo (`joblib`) e disponibilização via API REST (FastAPI) para o sistema de captação.
  - **Evidência:** `docs/02_implementacao_monitoramento.md` (seção 6.1).
- **6.2 Plano de monitoramento** — *Realizado*
  - **Descrição:** Rotina de monitoramento de *data drift* (mensal) e *model drift* (trimestral), com gatilho de retreinamento caso o MAPE ultrapasse 12%.
  - **Evidência:** `docs/02_implementacao_monitoramento.md` (seção 6.2).
- **6.3 Relatório e apresentação final** — *Realizado*
  - **Descrição:** Consolidação dos resultados no `README.md`, nos notebooks executados e neste relatório espelho da A1.
  - **Evidência:** `README.md` e `docs/relatorio_final_A1.md`.
- **6.4 Revisão do projeto** — *Realizado*
  - **Descrição:** Registro das lições aprendidas e oportunidades de evolução (inclusão de estado de conservação e reformas).
  - **Evidência:** `docs/02_implementacao_monitoramento.md` (seção 6.4).

## Síntese Final
- **7.1 Comece pelo negócio** — *Realizado* | Evidência: `docs/01_entendimento_negocio.md` e `README.md`.
- **7.2 Respeite o atrito** — *Realizado* | Evidência: `notebooks/02_preparacao_dados.ipynb` e `README.md`.
- **7.3 Abrace a iteração** — *Realizado* | Evidência: `notebooks/03_modelagem_avaliacao.ipynb` (Iteração 1 vs. 2) e `README.md`.
- **7.4 Mensure o impacto** — *Realizado* | Evidência: `notebooks/03_modelagem_avaliacao.ipynb` (seção 5.1) e `README.md`.
- **7.5 Documente a jornada** — *Realizado* | Evidência: Repositório completo, `docs/` e `README.md`.
```[cite: 14, 15, 16, 17, 18, 25]

---

### PASSO 6 (FINAL): Subir tudo para o GitHub

No terminal do VS Code, execute:

```powershell
git add .
git commit -m "feat: projeto CRISP-DM completo (Fases 1 a 6 e relatorio A1)"
git push origin main