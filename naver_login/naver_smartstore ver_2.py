from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

# 셀레니움 - argument 설정 - 크롬드라이버 위치 설정
options = webdriver.ChromeOptions()
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')  # user_argument를 사람처럼 수정함
driver = webdriver.Chrome('/Users/euncheal/chromedriver', options=options)


# 스토어 주소 입력
store_url = "https://smartstore.naver.com/littledaisy2019/products/4965824636?NaPm=ct%3Dkwoucw7s%7Cci%3Dc21c199fc28373f00a24565e274e2f29ff1159d9%7Ctr%3Dslsl%7Csn%3D1055642%7Chk%3D1aabe53723626f5d73e6e604be349fb22b8723e6"
#store_url = "https://smartstore.naver.com/mato/products/491325765?NaPm=ct%3Dkxdfmn68%7Cci%3D7b414bb0b9aa74b0f39bc1fbc68e414bb5197327%7Ctr%3Dslsl%7Csn%3D347516%7Chk%3D775d9631e33beacb15931c9dfba6b9becf53a35a"


#키1 = 옵션1, 키2 = 옵션2, value = 가격


# 옵션 버튼은 항상 처음부터 찾아야함 그래서 함수로 구현해서 불러올때마다 새로운 값으로 인식시킴


def item_option(x):
    return driver.find_element_by_tag_name('body').find_elements_by_class_name('bd_3hLoi')[x]


# 스토어 주소를 항상 바꿀수있게 함수로 만듬

def get_smartstore(store_url):

    driver.get(store_url)  # url접속
    time.sleep(3)  # 접속 대기

# 옵션1부터 2까지를 전체 값 키값으로 지정한 딕셔너리 만들기


opt_dict = {}


def dict_func():

    item_option_list_1 = []  # 옵션1번을 받아올 빈 리스트
    item_option(0).click()  # 옵션1 버튼 클릭
    # 옵션1번값을 리스트로 저장 - 이후 딕셔너리에 키값으로 바뀜
    for i in item_option(0).find_element_by_tag_name('ul').find_elements_by_tag_name("li"):
        item_option_list_1.append(i.text)

    # 옵션1번리스트 딕셔너리 키값으로 바꿈
    opt_dict = dict.fromkeys(item_option_list_1)

    for j in item_option_list_1:

        item_option_list_2 = []  # 옵션2번 택스트를 저장할 2번째 빈 리스트

        driver.find_element_by_link_text(
            j).click()  # 옵션1번리스트의 택스트를 하나씩 검색해서 클릭한다
        item_option(1).click()  # 옵션2번 버튼 클릭한다

        # 옵션2번 택스트 리스트로 저장
        for x in item_option(1).find_element_by_tag_name('ul').find_elements_by_tag_name("li"):
            item_option_list_2.append(x.text)

        # 옵션2리스트의 값을 옵션1을 키값으로한 딕셔너리로 만듬
        opt_dict[j] = dict.fromkeys(item_option_list_2)

        # 옵션1번 다시 클릭
        item_option(0).click()
    # 여기까지 옵션1부터 2까지를 전체 값 키값으로 지정한 딕셔너리 만들기


# opt_dict으로 만들어진 키값에 가격을 value로 저장하기

    def price():
        for i in opt_dict:
            # 옵션1번은 이미 위에서 딕셔너리 만들면서 클릭된 상태로 시작한다
            driver.find_element_by_link_text(i).click()  # 딕셔너리 키값으로 링크 옵션1 클릭
            for j in opt_dict[i]:
                item_option(1).click()  # 옵션2클릭

                # 옵션2번 값 클릭하고 가격 딕셔너리에 저장한후 물품삭제하여 다시 처음상태로 되돌린다
                # 이때 품절상품은 클릭이 안되면서 알러트가 나오고 이를 try문으로 처리하고 품절은 품절이라고 알려준다
                try:
                    driver.find_element_by_link_text(j).click()  # 옵션2링크 클릭
                    # 옵션1-2 클릭을 통해 얻은 가격 딕셔너리 값으로 저장
                    opt_dict[i][j] = driver.find_element_by_xpath(
                        """//*[@id="content"]/div/div[2]/div[2]/fieldset/div[8]/div[2]/strong/span""").text
                    # 옵션1-2를 클릭해서 생긴 결제창 닫음
                    driver.find_element_by_xpath(
                        """//*[@id="content"]/div/div[2]/div[2]/fieldset/div[7]/ul/li/button""").click()
                    # 옵션1 다시 클릭
                    item_option(0).click()
                    # 옵션1의 택스트 클릭
                    driver.find_element_by_link_text(i).click()
                except:
                    # 품절되면 알러트 뜨며 품절창 나옴 그래서 품절인걸 딕셔너리에 저장하고
                    # 알러트창 확인눌러서 닫음
                    # 그리고 다음으로 넘어감
                    opt_dict[i][j] = "품절입니다"
                    item_option(0).click()
                    driver.find_element_by_link_text(i).click()
                    pass
            item_option(0).click()  # 옵션1 다시 클릭

    price()
    item_name = driver.find_element_by_xpath(
        """//*[@id="content"]/div/div[2]/div[2]/fieldset/div[1]/div[1]/h3""").text
    print(item_name, "\n\n", opt_dict)
# 물품 이름 가져오기


get_smartstore(store_url)
dict_func()
