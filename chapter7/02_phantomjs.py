from selenium import webdriver

# PhantomJS 로딩
driver = webdriver.PhantomJS('./phantomjs')
# 화면 사이즈 & 해상도 조절
driver.set_window_size(1920, 1080)
# 네이버 들어가기 
driver.get('http://naver.com')
# 스크린샷 찍기
driver.get_screenshot_as_file('naver_main_phantomjs.png')
# 브라우저 종료 
driver.quit()
