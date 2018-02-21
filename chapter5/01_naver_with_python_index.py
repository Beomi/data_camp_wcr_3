import requests
from bs4 import BeautifulSoup as bs

url = 'http://naver.com'
res = requests.get(url)
html = res.text
soup = bs(html, 'lxml')

nav_titles = soup.select('#PM_ID_serviceNavi > li > a > span.an_txt')

print(nav_titles[3].text)
