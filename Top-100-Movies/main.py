import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movie_headings = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movie_headings]
movies = movie_titles[::-1]

with open("movies.text", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
