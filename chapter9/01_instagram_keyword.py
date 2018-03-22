import requests
import os

BASE_URL = 'https://www.instagram.com/graphql/query/'
QUERY_HASH = '298b92c8d7cad703f7565aa892ede943'  # 검색 Query Hash
SEARCH_KEYWORD = '강아지'

if not os.path.exists('./imgs'):
    os.mkdir('imgs')


def get_variables(tag_name, end_cursor=None):
    if not end_cursor:
        return '{"tag_name":"' + tag_name + '","first":0}'
    else:
        return '{"tag_name":"' + tag_name + '","first":0, "after":"' + end_cursor + '"}'


has_next_page = True
MAX_PAGE = 100
current_page = 0
res = requests.get(BASE_URL, params={
    'query_hash': QUERY_HASH,
    'variables': get_variables(SEARCH_KEYWORD)
})

while has_next_page and current_page < MAX_PAGE:
    res_json = res.json()
    has_next_page = res_json['data']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    end_cursor = res_json['data']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']

    edges = res_json['data']['hashtag']['edge_hashtag_to_media']['edges']

    for article in edges:
        img_url = article['node']['display_url']
        img_filename = img_url.split('/')[-1]
        img = requests.get(img_url)
        f = open('./imgs/' + img_filename, 'wb+')
        f.write(img.content)
        f.close()

    current_page += 1
    res = requests.get(BASE_URL, params={
        'query_hash': QUERY_HASH,
        'variables': get_variables(SEARCH_KEYWORD, end_cursor)
    })
