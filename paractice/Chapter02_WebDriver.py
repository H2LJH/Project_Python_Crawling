#               ===== chapter02_WebDriver.py =====
# * selenium의 WebDriver 사용방법(+Chrom Driver)
# * instagram 페이지에서 우너하는 해쉬태그로 selenium 접속(+ 크롬 드라이버)

from selenium import webdriver
driver = webdriver.Chrome(executable_path='../webDriver/chromedriver.exe')

# URL 주소의 한글을 유니코드로 변환(한글이면 깨지는 경우가 있음)
url = 'https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90/'
driver.get(url)










#driver.close() # 실행 후 브라우저 종료