from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

user_id = input("user_id")
user_pw = input("user_pw")


options = webdriver.ChromeOptions()
# user_argument를 사람처럼 수정함
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')


# 로그인이 되었는지 확인하기 위해 전체 과정이 끝나고 크롬창을 닫지 않음
options.use_chromium = True
options.add_experimental_option("detach", True)


# 백그라운드에서 실행하기
# options.add_argument("headless")


# 로그인페이지 접속
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver = webdriver.Chrome('/Users/euncheal/chromedriver', options=options)
driver.get(url)


def login(user_id, user_pw):
    # id 입력
    tag_id = driver.find_element_by_name('id')
    pyperclip.copy(user_id)
    tag_id.click()
    tag_id.send_keys(Keys.COMMAND, 'v')
    time.sleep(1)
    # password 입력 후 엔터
    tag_pw = driver.find_element_by_name('pw')
    pyperclip.copy(user_pw)
    tag_pw.click()
    tag_pw.send_keys(Keys.COMMAND, 'v',)
    time.sleep(1)
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()
    time.sleep(2)


login(user_id, user_pw)
