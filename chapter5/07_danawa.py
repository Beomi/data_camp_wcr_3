import requests
from bs4 import BeautifulSoup as bs

s = requests.Session()
s.get('https://auth.danawa.com/login')
s.headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
s.post('https://auth.danawa.com/login', data={
    'id': '다나와 ID',
    'password': '다나와 PW',
})
res = s.get('http://cws.danawa.com/point/index.php')
res.encoding = 'euc-kr' # 다나와 마이페이지는 encoding을 지정해줘야 합니다.
html = res.text

soup = bs(html, 'lxml')

my_name = soup.select_one('span.user_nick > strong')
# 내 ID가 나오면 성공!
print(my_name.text)
