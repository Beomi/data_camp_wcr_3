import requests
from bs4 import BeautifulSoup as bs

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'referer': 'https://www.inflearn.com/wp-login.php',
}

s = requests.Session()
s.headers = headers

data = [
    ('log', '인프런ID'),
    ('pwd', '인프런PW'),
    ('wp-submit', '\uB85C\uADF8\uC778'),
    ('redirect_to', 'https://www.inflearn.com'),
    ('testcookie', '1'),
]

# 쿠키 채우기용 로그인 페이지 방문
s.get('https://www.inflearn.com/wp-login.php')
# 로그인 POST 요청
s.post(
    'https://www.inflearn.com/wp-login.php',
    data=data
)
# 실제 크롤링할 페이지 방문
res = s.get('https://www.inflearn.com')
soup = bs(res.text, 'lxml')

name = soup.select_one('ul.topmenu > li:nth-of-type(1) > a > span')
print(name.text)
