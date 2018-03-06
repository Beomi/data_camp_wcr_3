from selenium import webdriver

# 크롬 옵션 추가하기
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 헤드리스모드 
options.add_argument('--disable-gpu') # 호환성용 (필요없는 경우도 있음)
options.add_argument('--window-size=1920x1080') # (가상)화면 크기 조절
# 크롬 모바일 버전으로 User Agent 설정하기 
options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36")
# 크롬 Options를 넣어준 Headless 모드 크롬
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
# 구글에서 'my user agent' 검색 하기 
driver.get('https://www.google.com/search?q=my+user+agent')
# User Agent 결과값 가져오기 
my_user_agent = driver.find_element_by_css_selector('.xpdopen').text
print(my_user_agent)
# 브라우저 및 드라이버 종료
driver.quit()
