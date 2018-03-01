from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('http://naver.com')

# CSS Selector를 통해 driver에서 요소 바로 찾아주기 
first_word = driver.find_element_by_css_selector('span.ah_k')
# 찾아준 요소의 text(본문) 가져오기
print(first_word.text)

driver.quit()
