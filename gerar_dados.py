import os
import numpy as np
import pandas as pd

np.random.seed(42)
n = 1200

# Garante que a pasta existe
os.makedirs("data/raw", exist_ok=True)

# 1. Tabela de Indicadores por Bairro (para integração na Fase 3 - Item 3.4)
bairros_info = pd.DataFrame({
    "bairro": ["Asa Sul", "Asa Norte", "Águas Claras", "Guará", "Taguatinga", "Samambaia", "Planaltina", "Sobradinho"],
    "renda_media_bairro": [12500, 11800, 8200, 6500, 4800, 3200, 2900, 5400],
    "indice_infraestrutura": [9.4, 9.2, 8.5, 7.8, 7.2, 6.1, 5.8, 7.5],
    "preco_m2_ref": [11500, 11000, 7800, 6800, 5200, 3800, 3100, 5500]
})
bairros_info.to_csv("data/raw/indicadores_bairros.csv", index=False)

# 2. Tabela Principal de Imóveis (com erros propositais para Itens 2.4 e 3.2)
bairros = np.random.choice(bairros_info["bairro"], size=n, p=[0.14, 0.14, 0.18, 0.12, 0.14, 0.10, 0.08, 0.10])
tipos = np.random.choice(["Apartamento", "Casa", "Kitnet"], size=n, p=[0.60, 0.28, 0.12])

areas = []
quartos = []
banheiros = []
vagas = []
idades = []
precos = []

ref_map = dict(zip(bairros_info["bairro"], bairros_info["preco_m2_ref"]))

for b, t in zip(bairros, tipos):
    if t == "Kitnet":
        area = np.random.normal(32, 6)
        q = 1
        ban = 1
        v = np.random.choice([0, 1], p=[0.6, 0.4])
    elif t == "Apartamento":
        area = np.random.normal(85, 28)
        q = int(np.clip(round(area / 32), 1, 4))
        ban = int(np.clip(q, 1, 4))
        v = np.random.choice([1, 2, 3], p=[0.5, 0.4, 0.1])
    else:  # Casa
        area = np.random.normal(180, 55)
        q = int(np.clip(round(area / 50), 2, 5))
        ban = int(np.clip(q, 2, 5))
        v = np.random.choice([1, 2, 3, 4], p=[0.15, 0.45, 0.25, 0.15])

    area = max(20, round(area, 1))
    idade = int(np.random.randint(0, 45))
    
    # Fórmula base de preço + ruído realista de mercado
    fator_idade = max(0.75, 1 - idade * 0.005)
    fator_vaga = 1 + (v * 0.04)
    preco_base = area * ref_map[b] * fator_idade * fator_vaga
    ruido = np.random.normal(1.0, 0.07)
    preco = round(preco_base * ruido, -2)

    areas.append(area)
    quartos.append(q)
    banheiros.append(ban)
    vagas.append(v)
    idades.append(idade)
    precos.append(preco)

df = pd.DataFrame({
    "id_imovel": range(1001, 1001 + n),
    "bairro": bairros,
    "tipo": tipos,
    "area_m2": areas,
    "quartos": quartos,
    "banheiros": banheiros,
    "vagas_garagem": vagas,
    "idade_imovel": idades,
    "condominio": np.where(tipos == "Casa", np.random.choice([0, 350, 600], size=n, p=[0.7, 0.2, 0.1]), np.round(np.array(areas) * np.random.uniform(7, 13, size=n), 2)),
    "preco_venda": precos,
    "cpf_proprietario": [f"***{np.random.randint(100,999)}.***-**" for _ in range(n)]  # Dado sensível p/ filtrar na Fase 3 (Item 3.1)
})

# --- Inserção proposital de problemas de qualidade (Item 2.4 e 3.2) ---
# 1. Valores ausentes (NaN)
df.loc[np.random.choice(df.index, 45, replace=False), "vagas_garagem"] = np.nan
df.loc[np.random.choice(df.index, 38, replace=False), "condominio"] = np.nan
df.loc[np.random.choice(df.index, 20, replace=False), "idade_imovel"] = np.nan

# 2. Erros de digitação / Outliers absurdos (estilo "monitor de 119 polegadas")
df.loc[10, "area_m2"] = 0.0
df.loc[25, "area_m2"] = 9500.0
df.loc[40, "preco_venda"] = 1.0
df.loc[55, "preco_venda"] = 95000000.0
df.loc[70, "quartos"] = 45

# 3. Inconsistência de texto
df.loc[100:115, "bairro"] = "asa sul"

# 4. Linhas duplicadas
df = pd.concat([df, df.iloc[:15]], ignore_index=True)

df.to_csv("data/raw/imoveis.csv", index=False)
print("Bases geradas com sucesso em data/raw/!")
print(f"imoveis.csv: {df.shape[0]} linhas x {df.shape[1]} colunas")
print(f"indicadores_bairros.csv: {bairros_info.shape[0]} linhas x {bairros_info.shape[1]} colunas")