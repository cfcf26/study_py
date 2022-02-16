#정규표현식으로 텍스트 패턴 찾기
import re #파이썬의 모든 정규식 기능은 re모튤에 있다

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #re.compile 는 정규표현식을 나타내는 문자열값을 전달하면 Rebex 패턴객체(또는 단순히 Regex 객체)를 돌려받는다 라는데 이게 뭔말이야......
#자 이해한대로 적어보자... 흠... 하.... 그러니까 re.compile는 정규표현식을 변환하는 거다?

mo = phoneNumRegex.search('my number is 123-456-7890.')
print('phone number found : ' + mo.group())
#설명 드가자 그니까 re.compile(r.\d~)는 정규표현식을 정해준거고 .serch는 그 정규표현식에 맞는게 있는지 찾아주는거고 .group은 search에서 찾은 택스트를 가지고있는거
#그래서 컴파일에서 정해준 정규표현식에 맞는 폰번호를 찾아냈고 그게 123~어쩌구 이고 그걸 그룹이 가지고있게되었고 프린트가 그걸 가져다가 표시해준거다
#아 이해된다
#기억하자 re.compile .search .group
#잠깐만 그럼 원래라면 re.comile.search re.compile.group 이라고 작성해야했던거네? 이쪽이 좀더 이해하기 쉬워보이는데 이게 맞는건가?

##실험해보자!

print('폰번호 찾았다 : ' + re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d').search('내 폰번호는 010-3858-9932').group())
##실험에 성공하였다 지식이 +1 상승하였다

###실험2
###그렇다면 정규표현식은 고정해두고 search값을 바꿔서 찾을수있게 함수로 바꿀수 있는건가??

def 함수로만들기(말해봐):
    말해봐1 = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
    말해봐2 = 말해봐1.search(말해봐)
    print('이거 말한거 맞냐? ' + 말해봐2.group())
    return 말해봐


print('말해봐')
함수로만들기(input())
### 성공은 했는데 왜 1,2 단계로 나눠야 성공하고 같이 한줄로 묶으면 실패하지??


def 함수로만들기2(말해봐):
    print('이거 말한거 맞냐? ' + re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d').search(말해봐).group())
    return 말해봐

함수로만들기2(input())
### 되네? 근데 이거 실패하니까 문제가 발생하내 이번엔 실패하면 실패했다고 뜨게 만드는거 하자
### 일단 좀 자고...
