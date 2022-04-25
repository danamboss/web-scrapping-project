from bs4 import BeautifulSoup
import requests

url = 'https://sharonbandele.me/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features="html5lib")
prttysp = soup.prettify()

print(prttysp)


"""for link in soup.find_all('a'):
  print(link.get('href'))"""