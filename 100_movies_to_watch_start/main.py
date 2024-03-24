import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
website_text = response.text

soup = BeautifulSoup(website_text,"html.parser")

all_movies = soup.find_all(name = "h3" , class_="title")
# print(all_movies)

movie_title=[movie.getText() for movie in all_movies]

# for n in range (len(movie_title)-1 ,-1,-1):
#     print(movie_title[n])

movies = movie_title[::-1]

with open("movies.txt","w") as file:
    for movie in movies:
        file.write(f"{movie}\n")