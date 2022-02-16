#strip의 정규식 버전 만들기 - try_2...

#기존 코드의 문제점 1 - 애초에 문제 이해를 잘못함
#뭘 잘못했느냐 - 제거할 문자를 정해주지 않으면 좌우의 공백 제거 << 문제에서는 정리할 문자열 말고
#다른 매개변수를 전달받지 않았다면 문자열의 앞과 끝에서 제거된다 라고 했다
#이것부터 이해하는게 첫번째 스텝인듯하다
#잘 모르겠으니 그냥 strip()을 사용해보자

#whilt space 제거

# #아래 택스트를 보면 문장 좌우에 공백이 있다
# text = ' Water boils at 100 degrees '
# print('[' + text.rstrip() + ']') #[ Water boils at 100 degrees]
# print('[' + text.lstrip() + ']') #[Water boils at 100 degrees ]
# print('[' + text.strip() + ']')  #[Water boils at 100 degrees]

#각 함수에 따라 좌나 우 혹은 양쪽다 공백이 제거된 값만 출력되었다

#그럼 이제 내가 해야될건 이것부터 만들어보자
import re
# def strip_Regex(text):
#     test_Regex = re.compile(r'^(\s)*(.*?)(\s)*$')
#     mo = test_Regex.search(text)
#     print(mo.group(2))


#text=text.replace("_","").replace(" ", "")
#print(text)
# strip_Regex(input())
    

#첫번째 스탭 드디어 성공함.... 하... 이거하나때문에 4일걸림... 하...

#두번째 해야될일
#함수의 두 번째 매개변수로 지정된 문자가 문자열에서 제거된다
#그러니까 인풋두개 받아서 첫번째꺼는 탐색될 대상 두번째는 탐색할것 으로 생각하고
#첫번째에서 두번째를 걸러내고 나머지만 나오면됨

def strip_Regex2(string,text):
    #test_Regex = re.compile('^'+text+'*'+r'(.*?)'+text+'*$') #1트 실패함
    test_Regex = re.compile(
        '^' + text + '*' +    # Zero or more of the characters to be stripped on left side of content
        r'(.*?)' +  # Defines unstripped content as the only group. Nongreedy so as not to include characters to be stripped on right side 
        text + '*$')

    mo = test_Regex.search(string)
    #string = mo.group(1)
    #print(string)
    print(mo)

strip_Regex2('**SpamSpamBaconSpamEggsSpamSpam','[ampS*]')
