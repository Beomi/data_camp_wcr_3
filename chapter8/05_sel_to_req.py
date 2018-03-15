import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

QUERY_HASH = 'd6f4427fbe92d846298cf93df0b937d3'
# 이부분을 채워주세요! (크롬 네트워크탭 참조)
# 이 값은 언제든 바뀔 수도 있습니다

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.instagram.com/accounts/login/')

input_id = driver.find_element_by_css_selector('input[name="username"]')
# input_id = driver.find_element_by_name('username')
input_pw = driver.find_element_by_css_selector('input[name="password"]')
# input_pw = driver.find_element_by_name('password')

input_id.send_keys('인스타계정이메일')
input_pw.send_keys('인스타계정패스워드')
input_pw.send_keys(Keys.ENTER)

import time
time.sleep(2)

cookies = driver.get_cookies()

s = requests.Session()
s.headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36'
}
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'], secure=cookie['secure'])

driver.close()

res = s.get('https://www.instagram.com/graphql/query/?query_hash=' + QUERY_HASH)

for _ in range(50):
    edge_web_feed_timeline = res.json()['data']['user']['edge_web_feed_timeline']
    page_info = edge_web_feed_timeline['page_info']
    end_cursor = page_info['end_cursor']
    edges = edge_web_feed_timeline['edges']

    for edge in edges:
        node = edge['node']
        try:
            img_url = node['display_url']
        except Exception as e: # 이미지가 없는 게시글(친구 추천 등)
            continue
        img_name = img_url.split('/')[-1]
        img_body = s.get(img_url).content
        f = open('./imgs/{}'.format(img_name), 'wb+')
        f.write(img_body)
        f.close()
    new_url = 'https://www.instagram.com/graphql/query/'
    res = s.get(new_url, params={
        "query_hash": QUERY_HASH,
        "variables": '{"fetch_media_item_cursor":"' + end_cursor + '"}'
    })
