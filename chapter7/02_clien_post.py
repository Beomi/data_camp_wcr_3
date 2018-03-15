import requests
from bs4 import BeautifulSoup as bs

main_url = 'https://www.clien.net/service/group/community?po='

s = requests.Session()
s.headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36'
}

def get_url_list_by_page(page_num):
    _urls = []
    res = s.get(main_url + page_num)
    html = res.text
    soup = bs(html, 'lxml')
    comments_exist_posts = soup.select('a.list_reply')
    for cep in comments_exist_posts[1:]: # 1st 공지 제외 
        _url = 'https://www.clien.net' + cep['href']
        _urls.append(_url.split('?')[0])
    return _urls

def get_url_list_all():
    url_list = []
    for i in range(10): # 0 ~ 9
        page_num = str(i)
        url_list += get_url_list_by_page(page_num)
    return url_list

def get_post_title(soup):
    title_el = soup.select_one('h3.post_subject')
    title = title_el.text.strip()
    return title

def get_post_body(soup):
    body_el = soup.select_one('div.post_content')
    body = body_el.text.strip()
    return body

def get_post_comments(url):
    res = s.get(url + '/comment')
    soup = bs(res.text, 'lxml')
    comments = []
    for el in soup.select('div.comment_view'):
        comments.append(el.text.strip())
    return comments

def get_post(url):
    res = s.get(url)
    soup = bs(res.text, 'lxml')
    title = get_post_title(soup)
    body = get_post_body(soup)
    comments = get_post_comments(url)
    return {
        'title': title,
        'body': body,
        'comments': comments
    }

if __name__=='__main__':
    url_list = get_url_list_all()

    post_list = []

    for url in url_list: 
        post = get_post(url)
        post_list.append(post)
    
    print(post_list[:10]) # 앞 10개만 출력 
