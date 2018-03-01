from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

# 네이버 로그인 페이지
driver.get('https://nid.naver.com/nidlogin.login')
# ID/PW 입력하고 로그인 버튼 클릭
driver.find_element_by_css_selector('#id').send_keys("네이버아이디")
driver.find_element_by_css_selector('#pw').send_keys("네이버패스워드")
# 로그인 버튼을 누르는 경우:
# driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()
# 로그인 폼을 전송하는 경우:
driver.find_element_by_css_selector('form').submit()

# 네이버 가입 카페 목록 가져오기
driver.get('http://section.cafe.naver.com/')

# 카페 목록 더보기 버튼 클릭 
while True:
    try:
        driver.find_element_by_css_selector('#PageArea > a.btn_view').click()
    except Exception as e:
        # '더보기' 버튼이 더이상 없는 경우, Loop를 빠져나가기
        break

# 카페 목록 가져오기 
cafe_list = driver.find_elements_by_css_selector('div.list_content > p.tit > a')

for cafe in cafe_list:
    print(cafe.text)

driver.quit()
