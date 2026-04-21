import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")
print("Data loaded! Here are our movies:")
print(movies["title"].tolist())

cv=CountVectorizer()
vectors = cv.fit_transform(movies["genres"])

print("\n Genres converted to vectors ")

similarity = cosine_similarity(vectors)

print("Similarity scores calculated!")
print(f" Grid size: {similarity.shape} (15 movies x 15 movies)")

def recommend(movie_title):
    if movie_title not in movies["title"].values:
        print(f"{movie_title} not found in our list1")
        return
    index = movies[movies["title"]== movie_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x:x[1], reverse=True)
    top5 = scores[1:6]

    print(f"\n because you liked '{movie_title}', we recommend:")
    for i, (idx,score) in enumerate(top5):
        print(f" {i+1}.{movies['title'][idx]} (similarity: {round(score,2)})")


recommend("Inception")
recommend("3 Idiots")
recommend("KGF")