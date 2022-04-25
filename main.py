from bs4 import BeautifulSoup
import requests

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