from bs4 import BeautifulSoup
import requests
import json

url = 'https://sharonbandele.me/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features="html5lib")
prttysp = soup.prettify()

print(soup.title)
print(soup.get_text)

tags = soup.find_all('a')

for link in tags:
  print(link.get('href'))


url2 = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

rv = requests.get(url2)

json_data = rv.json()

pizza_extract = json_data['query']['pages']['24768']['extract']

print(pizza_extract)