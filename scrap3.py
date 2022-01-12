from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')


def PRINT(string):
    print(string)


count = 1

# output name, price and number
for i in items:
    name = i.find('h4', class_='card-title').text.strip('\n')
    price = i.find('h5').text
    PRINT(f'{count}. Price: {price} Name: {name}')
    count = count + 1

# finding next page, find links
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

# add page number to url
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum is not None:
        x = link.get('href')
        urls.append(x)

PRINT(urls)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i in items:
        name = i.find('h4', class_='card-title').text.strip('\n')
        price = i.find('h5').text
        PRINT(f'{count}. Price: {price} Name: {name}')
        count = count + 1
