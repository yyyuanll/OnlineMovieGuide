import pandas as pd
import os

root_path = r'C:/Users/14472/Desktop/collection/Database/final project/OnlineMovieGuide/backend/images'
df = pd.read_excel('film.xlsx', usecols=['Title', 'imdbID','Poster'])
titles, imdbIDs, Posters = df['Title'].values, df['imdbID'].values, df['Poster'].values

for i, t in enumerate(imdbIDs):
    t = str(t)
    for root,dirs,files in os.walk(root_path):
        if t not in files:
            Posters[i] = 'N/A'
            print(Posters[i])