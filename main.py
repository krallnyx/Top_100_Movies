import requests
from bs4 import BeautifulSoup

URL = "https://www.afi.com/afis-100-years-100-movies/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = [title.getText() for title in soup.find_all("h6", class_="q_title")[:100]]

with open("movies.txt", "w") as file:
    [file.write(f"{movie}\n") for movie in all_movies]