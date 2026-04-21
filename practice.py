movies =[
    {"title": "Interstellar", "genre":"Sci-Fi", "rating":9.0},
    {"title": "KGF", "genre":"Action", "rating":8.5},
    {"title": "RRR", "genre":"Action", "rating":8.8},
    {"title": "Inception", "genre":"Sci-Fi", "rating":9.3},
    {"title": "3 Idiots", "genre":"Comedy", "rating":8.9},
]

def find_by_genre(movies_list, genre):
    result =[]
    for movie in movies_list:
        if movie["genre"] == genre:
            result.append(movie["title"])
    return result

def top_rated(movies_list):
    best = movies_list[0]
    for movie in movies_list:
        if movie["rating"]>best["rating"]:
            best = movie
    return best["title"]

print("Sci-Fi movies: ", find_by_genre(movies,"Sci-Fi"))
print("Action movies:",find_by_genre(movies,"Action"))
print("Top rated movie:", top_rated(movies))