import random as r
import string as s

# 문자 및 숫자 리스트를 생성
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","y","s","t","u","v","w","x","y","z"]
num = [1,2,3,4,5,6,7,8,9,0]

# 숫자 리스트를 문자열로 변환처리 (귀찮으니까)

#map 이 뭐지..?
num = list(map(str, num))

# 변환된 숫자 문자열과 문자열을 합쳐서 문자풀을 생성
string_pool = alp + num


#string_pool = s.ascii_uppercase + s.digits
#왜 i를 쓴거지? i 어디감????????
#아.. i라는 라는 식을 range만큼 반복하는거
#그럼 여기서 i라는 식은 result += r.choice(string_pool).upper() 이거 구나
#그게 아니고 i라는 변수를 식에 range만큼 대입하는건데 여기서 i는 필요없음 그래서 안나오는거임 ㅇㅇ...

# 난수 최대 길이 지정


"""
#원래식
number_max_digit = 18
result = ""
for i in range(number_max_digit):
    
   # 18 자리의 영문 숫자조합 난수를 생성한다.
    
    result += r.choice(string_pool).upper()

print(result)
"""
# 함수로 만들어서 길이 맘대로 바꿔보자

def nummax(num):
    number_max_digit = num
    result=""
    for x in range(number_max_digit):
        result += r.choice(string_pool).upper()   
    return result









# 고객 정보 입력
"""client_number = int(input("고객번호 : "))
client_code = str(input("고객 알파벳 :"))
carrier = input("배송사 :")"""

#이걸 while 로 맞을때까지 시켜보자
"""
if alp[client_number % 26] == client_code:
    print(nummax())
else:
    print("다시 실행하세요")
"""

while True:
    client_number = int(input("고객번호 : "))
    client_code = str(input("고객 알파벳 :"))
    max_number = int(input("몇자리? : "))

    if alp[client_number % 26] == client_code:
        print(nummax(max_number))
        break
    else:
        print("다시 실행하세요")
