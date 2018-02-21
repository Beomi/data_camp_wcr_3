import requests
from bs4 import BeautifulSoup as bs

s = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/64.0.3282.167 Safari/537.36',
    'Referer': 'https://login.coupang.com/login/login.pang',
    'X-Requested-With': 'XMLHttpRequest',
}

s.headers = headers

s.get('https://login.coupang.com/login/login.pang')

data = [
    ('email', '이메일주소'),
    ('password', '패스워드'),
]

s.post('https://login.coupang.com/login/loginProcess.pang', data=data)

response = s.get('http://cart.coupang.com/cartView.pang')

soup = bs(response.text, 'lxml')

cart_items = soup.select('#cartTable-other div.product-name-part > a')

for item in cart_items:
    print(item.text)
