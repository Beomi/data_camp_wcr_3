from selenium import webdriver

# 크롬 옵션 추가하기
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 헤드리스모드 
options.add_argument('--disable-gpu') # 호환성용 (필요없는 경우도 있음)
options.add_argument('--window-size=1920x1080') # (가상)화면 크기 조절
# 크롬 Options를 넣어준 Headless 모드 크롬
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
# 아래 URL로 이동
driver.get('http://naver.com')
# 스크린샷 찍기
driver.save_screenshot('naver.png') # .png만 됩니다.
# 브라우저 및 드라이버 종료
driver.quit()
