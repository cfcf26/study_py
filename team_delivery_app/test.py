from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select


# user_argument를 사람처럼 수정함
options = webdriver.ChromeOptions()
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')  # user_argument를 사람처럼 수정함
# chrome_options.add_argument("--kiosk-printing") 이건 크롬드라이버의 설정에서 프린터페이지를 불러오지않고 바로 인쇄하게 하는 옵션이다


driver1 = webdriver.Chrome('/Users/euncheal/chromedriver', options=options)
# 로그인이 되었는지 확인하기 위해 전체 과정이 끝나고 크롬창을 닫지 않음
options.use_chromium = True
options.add_experimental_option("detach", True)
driver1.get(url='https://www.naver.com/')
# THIS IS THE PRINT DIALOG WINDOW - This could be -1 depending on how many windows are opened
driver1.execute_script("document.body.style.zoom='100%'")
time.sleep(5)
driver1.execute_script('window.print();')
time.sleep(1000)
