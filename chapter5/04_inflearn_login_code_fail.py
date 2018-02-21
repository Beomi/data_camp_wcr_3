import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.inflearn.com/wp-login.php'

s = requests.Session()
s.get(url)

s.post(url, data={
    'log': '인프런ID',
    'pwd': '인프런PW',
})

res = s.get('https://www.inflearn.com/')
soup = bs(res.text, 'lxml')

name = soup.select_one('ul.topmenu > li:nth-of-type(1) > a > span')

# 내 이름이 나와야 하지만... "로그인" 이 나온다!
print(name.text)
