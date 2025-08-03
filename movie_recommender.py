
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'Movie': ['Inception', 'Interstellar', 'Tenet', 'The Dark Knight', 'Memento'],
    'Action': [1, 1, 1, 1, 1],
    'Sci-Fi': [1, 1, 1, 0, 0],
    'Drama': [1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
features = df.drop('Movie', axis=1)
similarity = cosine_similarity(features)

movie_name = input("Enter a movie you like: ").strip().title()

if movie_name in df['Movie'].values:
    index = df[df['Movie'] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]
    print("Recommended Movies:")
    for i in sorted_scores[:3]:
        print("-", df.iloc[i[0]]['Movie'])
else:
    print("Movie not found in database.")
