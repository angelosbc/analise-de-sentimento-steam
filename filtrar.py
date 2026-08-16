import pandas as pd
from tqdm import tqdm
import os

arquivo_gigante = 'steam_reviews.csv'
arquivo_saida = 'steam_reviews_brazilian.csv'
chunk_size = 100_000

print(f"Lendo '{arquivo_gigante}' e filtrando avaliações em PT-BR...")
primeiro_chunk = True
total = 0

for chunk in tqdm(pd.read_csv(arquivo_gigante, chunksize=chunk_size, low_memory=False)):
    filtro = chunk['language'].astype(str).str.lower().isin(['brazilian', 'portuguese', 'pt'])
    df_filtrado = chunk[filtro]
    
    if not df_filtrado.empty:
        total += len(df_filtrado)
        if primeiro_chunk:
            df_filtrado.to_csv(arquivo_saida, index=False, mode='w', encoding='utf-8')
            primeiro_chunk = False
        else:
            df_filtrado.to_csv(arquivo_saida, index=False, mode='a', header=False, encoding='utf-8')

print(f"\n✅ Concluído! {total:,} avaliações salvas em '{arquivo_saida}'.")
