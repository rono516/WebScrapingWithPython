# pip install requests
# pip install requests-html
from requests_html import HTMLSession

# create session
session = HTMLSession()

# url = f"https://www.google.com/search?q=weather+{query}"
query = 'nairobi'
url = f"https://www.google.com/search?q=weather+{query}"

# create request
request = session.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

temp = request.html.find('span#wob_tm', first=True).text
symbol = request.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
description = request.html.find('span#wob_dc', first=True).text
print(f'{query} is {temp + symbol} {description}')
