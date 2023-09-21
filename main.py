import pandas as pd

# Extration:
data = pd.read_csv('data/spotify_most_streamed.csv')

# Transformation:
data['Artist'] = data['Artist and Title'].str.split('-').str[0]

somas_por_artista = {}

for artist in data['Artist'].unique():

    filtro = data['Artist'] == artist
    
    data.loc[filtro, 'Streams'] = data.loc[filtro, 'Streams'].str.replace(',', '', regex=True).astype(float)
    
    soma_streams = data[filtro]['Streams'].sum()
    
    somas_por_artista[artist] = soma_streams

for artist, soma in somas_por_artista.items():
    print(f'Artista: {artist}, Soma das Streams: {soma}')