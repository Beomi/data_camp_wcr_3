from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('https://mbasic.facebook.com/login')
driver.find_element_by_css_selector('#m_login_email').send_keys('이메일주소')
driver.find_element_by_css_selector('input[name="pass"]').send_keys('페이스북패스워드')
driver.find_element_by_css_selector('form').submit()

driver.get('https://mbasic.facebook.com/stories.php')

for _ in range(10):
    _posts = driver.find_elements_by_css_selector('div[role="article"]')

    for post in _posts:
        title = post.find_element_by_css_selector('h3')
        contents = post.find_elements_by_css_selector('div > span > p')
        content = ''
        for con in contents:
            content += con.text.strip()
        if not content:
            continue
        print('제목: ', title.text)
        print('본문: \n', content.strip())
        print('-'*79)

    driver.find_element_by_css_selector('a[href^="/stories.php"]').click()

driver.quit()