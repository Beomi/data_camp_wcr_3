import requests
from bs4 import BeautifulSoup as bs

main_url = 'https://www.clien.net/service/group/community'

s = requests.Session()
s.headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36'
}

res = s.get(main_url)
html = res.text
soup = bs(html, 'lxml')

print('====== 모든 글들 URL ======')

# 글 전체 가져오기 
titles = soup.select('a.list_subject')
# titles 앞 두개는 공지사항 & 광고
for i in titles[2:]:
    # 글 가져오기 
    print(i.text.strip().split('\n')[1])
    # 글 URL 가져오기 
    print('https://www.clien.net' + i['href'])

# '댓글 숫자'를 클릭해서 글에 들어갈 수 있다.
# 즉, 댓글 숫자에 달린 a 태그를 찾아 댓글이 있는 글들의 URL을 가져와봅시다.

print('====== 댓글 있는 글들 URL ======')

comments_exist_posts = soup.select('a.list_reply')
for cep in comments_exist_posts:
    print(cep.text.strip())
    print('https://www.clien.net' + cep['href'])
