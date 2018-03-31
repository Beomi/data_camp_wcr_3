import requests
import re

res = requests.get('http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=005&aid=0001085058&m_view=1&includeAllCount=true&m_url=%2Fcomment%2Fall.nhn%3FserviceId%3Dnews%26gno%3Dnews005%2C0001085058%26sort%3Dlikability')
html = res.text

pattern = re.compile('(\d{4}-\d{2}-\d{2} \d{2}:\d{2})')


date = pattern.findall(html)

print(date)
