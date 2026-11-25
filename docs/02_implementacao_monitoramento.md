# Fase 6: Implementação e Monitoramento

## 6.1 Plano de Implementação (Arquitetura)
- **Serialização do Modelo:** O modelo vencedor (`GradientBoostingRegressor` tunado) é exportado via `joblib` juntamente com a pipeline de pré-processamento (imputação, *feature engineering* e *One-Hot Encoding*).
- **Integração com o Negócio:** Disponibilização do modelo através de uma API REST leve (FastAPI) consumida pelo sistema interno de captação da imobiliária. Ao preencher os dados do imóvel (bairro, tipo, área, quartos, banheiros, vagas, idade e condomínio), o corretor recebe instantaneamente a faixa de preço sugerida ($\pm 9\%$).

## 6.2 Plano de Monitoramento (Obsolescência / Drift)
- **Data Drift:** Monitoramento mensal da distribuição de área, condomínio e novos bairros cadastrados para detecção de desvios em relação à base de treino.
- **Model Drift (Obsolescência):** Comparação trimestral entre o preço sugerido pelo modelo e o valor real efetivado nas escrituras de venda.
- **Gatilho de Retreino:** Caso o MAPE em produção ultrapasse o limite de negócio ($12\%$) ou haja mudança macroeconômica relevante (ex: alteração brusca na taxa Selic), dispara-se o retreinamento automático com os novos dados consolidados.

## 6.3 Relatório e Apresentação Final
- Consolidação de todas as evidências técnicas nos notebooks (`notebooks/01_entendimento_dados.ipynb`, `02_preparacao_dados.ipynb` e `03_modelagem_avaliacao.ipynb`) e no espelho completo do checklist da Avaliação A1 (`docs/relatorio_final_A1.md`).

## 6.4 Revisão do Projeto (Lições Aprendidas)
- **O que funcionou bem:** A integração com indicadores socioeconômicos por bairro (`indicadores_bairros.csv`) e a remoção de outliers extremos elevaram drasticamente a estabilidade dos modelos baseados em árvores.
- **Limitações e Próximos Passos:** A base atual não contempla variáveis qualitativas (estado de conservação, reforma recente, posição solar). Incluir esses atributos na próxima iteração tende a reduzir ainda mais o erro em imóveis de alto padrão.