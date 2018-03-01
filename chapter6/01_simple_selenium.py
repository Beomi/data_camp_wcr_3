from selenium import webdriver

# 크롬 driver를 통해 크롬 실행
driver = webdriver.Chrome('./chromedriver')
# 아래 URL로 이동
driver.get('http://naver.com')
# 브라우저 및 드라이버 종료
driver.quit()