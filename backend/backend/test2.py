import json

with open('Recommend_dictionary.json', 'r', encoding='utf-8') as f:
        movie_dics = json.load(f)
i = 0
for key in movie_dics:
    i += 1
print(i)