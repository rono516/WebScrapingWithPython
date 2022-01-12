# set site url
# url = 'http://quotes.toscrape.com/'
from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com/'

# request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_="tags")

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quotetag in quoteTags:
        print(quotetag.text)


# PRINT(quotes)
