# Chapter04_Facebook_Login.py
# * : Selenium을 이용해서 페이스북 로그인
# * : 지속적으로 사용 불가능.. 페이스북이 보안을 위해 로그인버튼의 선택자를 수시로 변경함

from selenium import webdriver

# selenium을 사용해서 facebook에 로그인!
path = '..'
driver = webdriver.Chrome(executable_path='{}/webDriver/chromedriver.exe'.format(path))
url = 'https://www.facebook.com/'
driver.get(url) # 웹 드라이버로 URL페이지 접속

driver.find_element_by_id('email').send_keys('ID')
driver.find_element_by_id('pass').send_keys('PWD')
driver.find_element_by_id('u_0_e').click() # !! 로그인 버튼은 보안조치 때문에 id 값 자꾸 변동함
