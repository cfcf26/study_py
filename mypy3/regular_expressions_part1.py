#작업자동화하기 파트1

#정규표현식 없이 텍스트 패턴 찾기 -1

"""def isPhoneNumber(text):

    if len(text) != 12: #len은 리스트의 길이를 알려줌 여기서는 text의 길이가 12개인지 확인하는것
        return False
    for i in range(0, 3): 
        if not text[i].isdecimal(): #text에서 i번째 값이 숫자(.isdecimal)인지 확인하는것
            return False
    if text[3] != '-': #text의 4번째값(0부터 카운트 하니까 4이다)가 '-'인지 확인하는것
        return False
    for i in range(4, 7): 
        if not text[i].isdecimal(): #text에서 i번째 값이 숫자(.isdecimal)인지 확인하는것
            return False
    if text[7].isdecimal():
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('123-456-7890 is a phone number:')
print(isPhoneNumber('123-456-7890'))
print('mosi mosi is a phone number:')
print(isPhoneNumber('mosi mosi'))
"""
#정규표현식 없이 텍스트 패턴 찾기 -2
def isPhoneNumber(text):

    if len(text) != 12: #len은 리스트의 길이를 알려줌 여기서는 text의 길이가 12개인지 확인하는것
        return False
    for i in range(0, 3): 
        if not text[i].isdecimal(): #text에서 i번째 값이 숫자(.isdecimal)인지 확인하는것
            return False
    if text[3] != '-': #text의 4번째값(0부터 카운트 하니까 4이다)가 '-'인지 확인하는것
        return False
    for i in range(4, 7): 
        if not text[i].isdecimal(): #text에서 i번째 값이 숫자(.isdecimal)인지 확인하는것
            return False
    if text[7].isdecimal(): #text의 8번째값(0부터 카운트 하니까 8이다)가 '-'인지 확인하는것
        return False
    for i in range(8, 12):
        if not text[i].isdecimal(): #text에서 i번째 값이 숫자(.isdecimal)인지 확인하는것
            return False
    return True

message = 'call me at 123-456-7890 tomorrow. 123-456-0987 is my office.'



for i in range(len(message)): #i를 message 길이만큼 반복해라
    chunk = message[i:i+12] 
     
    if isPhoneNumber(chunk):
        print('Phon number found : ' + chunk)
print('Done')
# 이부분 이해안됨 [i:i+12]가 뭔말이여... 일단 이해한걸 적어보자...
"""i는 message의 길이만큼 들어감 그러면 처음에는 chunk = [0:12] 뭔말이냐면 0부터 12까지가 chunk가 된다
     그러면 머선일이 일어나느냐 call me at 1까지 isPhoneNumber에 넣어서 맞는지 확인한다
     당연히 아니라고 될거고 그러면 다시 i로 돌아가서 [1:13]이 chunk가 된다
     당연히 실패할거고 이걸 반복하다보면 123-456-7890 과 123-456-0987에 딱 맞는 두가지 경우만 if문을 통과할 수 있게된다
     그럼 여기서 쓰인 [i:i+12]는 범위를 설정해주는 거다 다른 리스트에서도 리스트 탐색 범위라던가 뭐 여러가지 범위 지정해줄때 이렇게 써먹으면 되는갑다 지식이 +1 상승했다"""