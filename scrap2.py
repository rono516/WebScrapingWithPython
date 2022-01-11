# set site url
url = 'http://quotes.toscrape.com/'
from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com/'

# request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
# PRINT(quotes)
