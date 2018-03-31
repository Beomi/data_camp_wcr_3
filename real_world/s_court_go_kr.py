import requests
from bs4 import BeautifulSoup as bs

headers = {
    'Origin': 'http://mglaw.scourt.go.kr',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,da;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'http://mglaw.scourt.go.kr/wsjs/panre/sjs060.do?q=%EC%82%B0%EC%97%85%EC%9E%AC%ED%95%B4',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = [
    ('q', '*'),
    ('w', 'panre'),
    ('section', 'panre_tot'),
    ('groups', '9,10,8'),
    ('outmax', '20'),
    ('pg', '1'),  # n 번째 페이지, 이 부분을 바꿔주며 json 요청 가능
    ('daewbyn', 'N'),
    ('smpryn', 'N'),
]

response = requests.post(
    'http://mglaw.scourt.go.kr/wsjs/panre/sjs050/panreList.do',
    headers=headers,
    data=data
)

dicts = response.json()

# dicts 내 'contId' 만 찾으면 각 판례의 URL 얻을 수 있음

# print(dicts)

# URL List 만들어주기

# 각 URL에 대해 for 문 돌며 아래 URL 크롤링

# 판례 Title 얻기:
'http://mglaw.scourt.go.kr/wsjs/panre/sjs100.do?contId=2229133'

# => JS코드 내 있어 정규 표현식 통해 찾아야 함
# ex) var bubNm='대법원';
# => re패턴: re.findall("var bubNm='(.+)'", res.text)[0] => '대법원'

# 실제 HTML 내:
# var contKindNm='판례';
# var contKindCd='01';
# var contId='2229133';
# var contIdEtc='';
# var saNo='2016두51429';
# var saNm='진폐재해위로금지급거부처분취소';
# var sngoDay= $.fmtWSdate('20170407');
# var bubNm='대법원';
# var panTypeNm='판결';

# 따라서 bubNm, sngoDay, saNo, panTypeNm 각각을 찾아 합쳐줘야 함
# => 대법원 2017. 4. 7. 2016두51429 판결

# 각 판례별 정보: http://mglaw.scourt.go.kr/wsjs/panre/sjs100/selDetail.do
# POST 방식으로 전송
res = requests.post(
    'http://mglaw.scourt.go.kr/wsjs/panre/sjs100/selDetail.do',
    data={
        'contId': '2229133', # 판례번호
        'hanjaYn': 'N'  # 고정값
    }
)

content = res.json()['search']['wmXml']
soup = bs(content, 'lxml')

title = soup.select_one('판례제목 CSS Selector')
contents = soup.select('판례 본문 CSS Selector')
