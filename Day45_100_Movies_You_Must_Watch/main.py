import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
content = BeautifulSoup(response.text, features='lxml')
movies = []
movie_titles = [movie.getText() for movie in content.find_all(name='h3', class_='title')]
movies = movie_titles[::-1]
with open("movies.txt", "w") as movies_data:
    for movie in movies:
        movies_data.write(movie + "\n")
print(movies)




