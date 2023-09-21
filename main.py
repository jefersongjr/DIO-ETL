import pandas as pd

# Extration:
data = pd.read_csv('data/spotify_most_streamed.csv')

# Transformation:
data['Artist'] = data['Artist and Title'].str.split('-').str[0]

data['Streams'] = data['Streams'].str.replace(',', '', regex=True).astype(float)
somas_por_artista = data.groupby('Artist', as_index=False)['Streams'].sum()
top_50_artistas_ordenados = somas_por_artista.sort_values(by='Streams', ascending=False).head(50)

print(top_50_artistas_ordenados)
