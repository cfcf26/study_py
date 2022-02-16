from selenium import webdriver
import time

# 셀레니움 - argument 설정 - 크롬드라이버 위치 설정
options = webdriver.ChromeOptions()
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')  # user_argument를 사람처럼 수정함
driver = webdriver.Chrome('/Users/euncheal/chromedriver', options=options)


# 스토어 주소 입력
store_url = "https://smartstore.naver.com/littledaisy2019/products/4965824636?NaPm=ct%3Dkwoucw7s%7Cci%3Dc21c199fc28373f00a24565e274e2f29ff1159d9%7Ctr%3Dslsl%7Csn%3D1055642%7Chk%3D1aabe53723626f5d73e6e604be349fb22b8723e6"


item_option_list_1 = []
itme_option_list_2 = []


def item_option(x):
    return driver.find_element_by_tag_name('body').find_elements_by_class_name('bd_3hLoi')[x]


def get_smartstore(store_url):

    # url 접속 전에 element를 찾으면 코드 진행이 불가능함으로 아직 아무런 element를 찾기 전에 반드시 url에 접속하여야 한다
    driver.get(store_url)
    time.sleep(3)  # 스토어 페이지가 완전히 로딩될때까지 기다리기

    # 옵션 선택값 전체선택 태그 네임으로 가져올때는 html상의 앞에 지정된 스타일에서 태그네임을 먼저 가져와서 오류가 생김으로 반드시 body에서 가져와야 문제가 생기지 않는다
    item_name = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[2]/div[2]/fieldset/div[1]/div[1]/h3')  # 물품 이름
    # 옵션 1번 클릭을 해서 aria-expanded의 값을 "false"에서 "true"로 바꿔야 이후에 리스트를 불러올수 있다
    item_option(0).click()
    items_option_list = driver.find_element_by_tag_name('body').find_element_by_class_name(
        'bd_3hLoi').find_element_by_tag_name(
        'ul').find_elements_by_tag_name("li")
    # 옵션 첫번째칸 설정 item_options의 elements는 복수 즉 전체 옵션창을 가져오는 것이고
    # 이건 element 단수 즉 첫번째 옵션창만 가져오는 것이다

    # 첫번째 옵션값의 택스트를 리스트값으로 저장하는 for문 이다
    for i in items_option_list:
        item_option_list_1.append(i.text)

    # 저장된 첫번째 옵션값의 택스트를 기준으로 첫번째 옵션값을 하나씩 클릭하고
    # 이후 두번째 옵션을 선택하여 클릭하고 그 옵션값 전부를 저장한다
    # 다음 두번째 옵션을 선택하기 위해 첫번째 옵션부터 다시 클릭을 이어나간다
    for j in item_option_list_1:
        driver.find_element_by_link_text(j).click()  # 옵션1의 값 하나씩 클릭
        item_option(1).click()  # 옵션2 버튼 클릭
        item_option2 = item_option(1).find_element_by_tag_name(
            'ul').find_elements_by_tag_name("li")
        for x in item_option2:
            itme_option_list_2.append(x.text)

        item_option(0).click()  # 옵션1 버튼 클릭

    print(item_name.text)  # 물품 이름 가져오기
    print(item_option_list_1, '\n\n', itme_option_list_2)


get_smartstore(store_url)
