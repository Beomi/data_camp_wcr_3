from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('http://naver.com')

# 여러 HTML elements 가져오기
new_words = driver.find_elements_by_css_selector('span.an_txt')

for word in new_words:
    print(word.text)

driver.quit()
