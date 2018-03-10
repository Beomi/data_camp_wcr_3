from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# PhantomJS Option 설정 
options = DesiredCapabilities.PHANTOMJS
# 모바일 크롬으로 user Agent 설정 
options["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36"

driver = webdriver.PhantomJS('phantomjs', desired_capabilities=options)

driver.get('https://www.google.com/search?q=my+user+agent')
my_user_agent = driver.find_element_by_css_selector('.xpdopen').text
print(my_user_agent)
driver.quit()
