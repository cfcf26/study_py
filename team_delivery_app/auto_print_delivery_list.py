from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

import time
# 셀레니움 - argument 설정 - 크롬드라이버 위치 설정
options = webdriver.ChromeOptions()
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')  # user_argument를 사람처럼 수정함
# chrome_options.add_argument("--kiosk-printing") 이건 크롬드라이버의 설정에서 프린터페이지를 불러오지않고 바로 인쇄하게 하는 옵션이다
options.add_argument("--kiosk-printing")

driver = webdriver.Chrome('/Users/euncheal/chromedriver', options=options)


# TODO: Stap1
# 1. 로그인 - ok
# 2. 배송대항 내역관리 접속 - ok
# 3. 배송상태 - 배송비 책정중 - ok
# 4. 배송메모 ‘[‘ 입력 - 검색버튼 클릭 - ok
# 5. 검색결과를 거래번호와 사용자 id를 각각의 리스트로 만들어서 2개의 리스트로 만든 후 불러올때 순서대로 각각 불러온다 -ok


# 1. 로그인
def login_admin():
    url = "https://admin3936.ableunion.com/"  # 어드민 주소 입력
    driver.get(url)
    driver.implicitly_wait(3)
    문어 = driver.find_element_by_xpath('//*[@id="frm"]/div[1]/input')
    문어.send_keys('냉장고')
    답어 = driver.find_element_by_xpath('//*[@id="frm"]/div[2]/input')
    답어.send_keys('너구리\n')
    # alert창 확인하기
    result = Alert(driver)
    result.accept()
    driver.implicitly_wait(3)


login_admin()

거래번호_list = []
고객id_list = []


def 배송비책정중_list():
    # 2. 배송대항 내역관리 접속
    url = 'https://admin3936.ableunion.com/delivery/list.jsp'
    driver.get(url)
    driver.implicitly_wait(10)
    # 3. 배송상태 - 배송비 책정중
    select = Select(driver.find_element_by_xpath(
        '//*[@id="page-wrapper"]/div[2]/div/div[2]/form/div/div[1]/div[1]/div[1]/select'))
    select.select_by_visible_text('배송비 책정중')
    # 4. 배송메모 ‘[‘ 입력 - 검색버튼 클릭
    배송메모 = driver.find_element_by_xpath('//*[@id="delivery_memo"]')
    배송메모.send_keys('[')
    driver.find_element_by_xpath(
        '//*[@id="page-wrapper"]/div[2]/div/div[2]/form/div/div[1]/div[7]/div[2]/input').click()
    driver.implicitly_wait(20)
    # 5. 검색결과를 거래번호와 사용자 id를 각각의 리스트로 만들어서 2개의 리스트로 만든 후 불러올때 순서대로 각각 불러온다
    for i in driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr'):
        거래번호_list.append(i.find_elements_by_tag_name('td')[1].text)
        고객id_list.append(i.find_elements_by_tag_name('td')[2].text)

    print(거래번호_list, 고객id_list)


배송비책정중_list()


# TODO: Stap 2
#  for I in 입력
# 	get(url) -ok
# 	배송메모 = 리스트_거래번호 [I] -ok
# 	고객id = 리스트_고객id[i] -ok
# 	검색버튼.click() -ok
# 	전체 체크박스 체크 -ok
# 	묶음리스트 인쇄 버튼 클릭 -ok
# 	로딩 기다림 -ok
# 	묶음리스트 인쇄 하기 - not ok....


def 묶음리스트():
    for i in range(1, len(거래번호_list)+1):
        #  for I in 입력
        # 	get(url)
        url = 'https://admin3936.ableunion.com/delivery/list.jsp'
        driver.get(url)
    # 	배송메모 = 리스트_거래번호 [I]
        배송메모 = driver.find_element_by_xpath('//*[@id="delivery_memo"]')
        배송메모.send_keys(거래번호_list[-i])
    # 	고객id = 리스트_고객id[i]
        고객id = driver.find_element_by_xpath('//*[@id="userid"]')
        고객id.send_keys(고객id_list[-i])
        driver.find_element_by_xpath(
            '//*[@id="page-wrapper"]/div[2]/div/div[2]/form/div/div[1]/div[7]/div[2]/input').click()
    # 	전체 체크박스 체크
        select_all = driver.find_element_by_name('_selected_all_')
        select_all.click()
    # 	묶음리스트 인쇄 버튼 클릭
        mergebtn = driver.find_element_by_name('mergebtn')
        mergebtn.click()
    # 	로딩 기다림
        driver.implicitly_wait(60)
    # 	묶음리스트 인쇄 하기 - ok!
    #   .execute_script는 크롬드라이버에서 js코드를 사용하는 코드이고 ()안에 js 코드를 넣어서 사용한다
        driver.execute_script('window.print();')
        time.sleep(1)

    # TODO: stap new 1
    # 프린트할 페이지 크기 72%로 바꾸기
    # 오버사이즈 표시
    # 그외 김과장님이 필요로한 요소 항상 찾아서 표시해주기





묶음리스트()


# TODO: Stap 3
# For I in 수정
#     Url = ‘https://admin3936.ableunion.com/delivery/list_detail.jsp?id=' + 	리스트_거래번호[I]+’&uid=‘ + 리스트_고객id[I]
#     Get.(url)
#     수정버튼.click()
#     배송메모 - 내용 바꾸기 - 수정날짜 ( ‘p’+yy-mm-dd)
#     수정버튼.click()
