from selenium import webdriver
import time

# 페이스북 그룹의 ID(숫자 혹은 문자열)를 넣어주세요.
GROUP_ID = 'pythonwebcrawling'

driver = webdriver.Chrome('./chromedriver')

driver.get('https://mbasic.facebook.com/login')
driver.find_element_by_css_selector('#m_login_email').send_keys('페이스북아이디')
driver.find_element_by_css_selector('input[name="pass"]').send_keys('페이스북비번')
driver.find_element_by_css_selector('form').submit()

driver.get('https://mbasic.facebook.com/groups/' + GROUP_ID)

for _ in range(10):
    current_url = driver.current_url
    _posts = driver.find_elements_by_css_selector('div[role="article"]')

    comment_urls = []

    for post in _posts:
        try:
            _url = post.find_element_by_css_selector("a[href*='view=permalink']")
            url = _url.get_attribute('href')
            # print(url)
            # print(''.join(url.split()))
            comment_urls.append(url)
        except Exception:
            pass
        title = post.find_element_by_css_selector('h3')
        contents = post.find_elements_by_css_selector('div > span > p')
        content = ''
        for con in contents:
            content += con.text.strip()

        title_text = title.text
        content = content.strip()

        print('제목: ', title_text)
        print('본문: \n', content)
        print('-'*79)

    comments = []

    for url in comment_urls:
        print(url)
        driver.get(url)
        # try:
        comment_list = driver.find_elements_by_css_selector('div[id^="ufi_"] > div > div > div[id]')
        for comment in comment_list:
            comments.append(comment.text)
    print('댓글:', '\n'.join(comments))
    driver.get(current_url)
    try:
        driver.find_element_by_css_selector('#m_group_stories_container > div:nth-child(2) > a[href^="/groups/"]').click()
    except Exception as e:
        print('No more pages!')
        break
# except Exception as e:
#     print(e)
driver.quit()