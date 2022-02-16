import random as r
import string as s
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","y","s","t","u","v","w","x","y","z"]
num = [1,2,3,4,5,6,7,8,9,0]

# 숫자 리스트를 문자열로 변환처리 (귀찮으니까)

#map 이 뭐지..?
num = list(map(str, num))

# 변환된 숫자 문자열과 문자열을 합쳐서 문자풀을 생성
string_pool = alp + num
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

#def max_random_number():


def nummax():
    number_max_digit = int(input("?"))
    result=""
    for x in range(number_max_digit):
        result += r.choice(string_pool).upper()   
    return(result)

print("난수로 만들고 싶은 난수의 길이를 설정하시오")
print(nummax())
print("난수로 만들고 싶은 난수의 길이를 설정하시오")
print(nummax())


