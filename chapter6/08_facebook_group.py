from selenium import webdriver

# 페이스북 그룹의 ID(숫자 혹은 문자열)를 넣어주세요.
GROUP_ID = 'pythonwebcrawling'

driver = webdriver.Chrome('./chromedriver')

driver.get('https://mbasic.facebook.com/login')
driver.find_element_by_css_selector('#m_login_email').send_keys('아이디')
driver.find_element_by_css_selector('input[name="pass"]').send_keys('패스워드')
driver.find_element_by_css_selector('form').submit()

driver.get('https://mbasic.facebook.com/groups/' + GROUP_ID)

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

    try:
        driver.find_element_by_css_selector('#m_group_stories_container > div:nth-child(2) > a[href^="/groups/"]').click()
    except Exception as e:
        print('No more pages!')
        break

driver.quit()