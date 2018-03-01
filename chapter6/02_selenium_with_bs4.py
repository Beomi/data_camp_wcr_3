from selenium import webdriver
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome('./chromedriver')

driver.get('http://naver.com')

# 현재 크롬 화면에 보이는 그대로 HTML 가져옴
html = driver.page_source

driver.quit()

# BeautifulSoup을 통해 HTML 요소 가져오기
soup = bs(html, 'lxml')

realtime_words = soup.select('span.ah_k')

for word in realtime_words:
    print(word.text)
