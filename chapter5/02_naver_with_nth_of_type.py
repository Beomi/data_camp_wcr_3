import requests
from bs4 import BeautifulSoup as bs

url = 'http://naver.com'
res = requests.get(url)
html = res.text
soup = bs(html, 'lxml')

nav_title = soup.select_one('#PM_ID_serviceNavi > li:nth-of-type(4) > a > span.an_txt')

print(nav_title.text)
