#졍규표현식 다시 살피기
import re
#괄호로 묶기

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')  
mo = phoneNumberRegex.search('내 폰번호는 010-1234-1234 입니다')
mo.group(1)
#010
mo.group(2)
#1234-1234
mo.group(0)
#010-1234-1234
mo.group()
#010-1234-1234
mo.groups()
#'010','1234-1234'  모든 그룹을 가져오려면 grop"s" 복수형을 기역하자
#차이점은 그룹들을 가져오는건 grops 일치하는 택스트 전체를 가져오는건 grop이다 기억하자
areacode, mainNumber = mo.groups()
#정규표현식으로 나누어 찾는 그룹은 2개임으로 변수도 2개를 지정해줘야 작동한다
print(areacode)
#010
print(mainNumber)
#1234-1234

#만약에 정규표현식에서 텍스트로서의 ()를 찾고싶다면? \를 앞에 붙여서 ()를 원시문자열로 바꿔주자!

phoneNumberRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d\d-\d\d\d\d)')
mo2 = phoneNumberRegex2.search('내폰번호는 (123) 1234-1234')
print(mo2.group(1))
#(123)
print(mo2.group(2))
#1234-1234

#파이프로 여러 그룹 대조하기

#파이프는 | 이다 \를 쉬프트누르고 누르면 나옴 or과 같은 뜻

heroRegex = re.compile(r'Batman|Tina Fay')
mo3 = heroRegex.search('Batman and Tina Fay')
print(mo3.group())
