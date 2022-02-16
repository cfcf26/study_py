#strip 대체해보기
#만들기전에 생각해보자
#만들어야하는 기능
#1.제거할 문자를 정해주지 않으면 좌우의 공백 제거
#그러면 (\\s)(r'\w+')(\\s) 그룹1제거 그룹2 살림 그룹3 제거 이렇게 하면 될듯?
#spaceStripRegex = re.compile(r'''
 #   ^(\s)*  # Left white space if any
 #   (.*?)   # String content
 #   (\s)*$  # Right white space if any
 #   ''', re.VERBOSE)




#2.제거할 문자를 정해주면 그 문자와 동일한 문자가 없을때까지 제거한다


import re

def make_strip(something,bulabula):
    if something == 0:
        bula_Regex = re.compile(r'''
            ^(\s)*  # Left white space if any
            (.*?)   # String content
            (\s)*$  # Right white space if any
            ''', re.VERBOSE).search(bulabula)
        print(bula_Regex.group(2))
    else:
        bula_some = re.compile(something).search(bulabula).group()
        print(bula_some)

print("찾을단어와 찾아야할 문장을 적으시오")
make_strip(input(),input())
