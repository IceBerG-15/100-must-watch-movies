import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(URL)
# print("encoding is", r.encoding)  # prints ISO-8859-1 (wrong)
r.encoding = "utf-8"              # tells r.text to use utf-8
soup = BeautifulSoup(r.text, "lxml")

titles=soup.find_all(name='h3',class_='title')
titles=titles[::-1]

length=len(titles)
with open('movies.txt','w') as file:  
    for title in titles:
        file.write(f'{title.text}\n')
