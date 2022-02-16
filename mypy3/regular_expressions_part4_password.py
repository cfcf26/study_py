import re

def check_password(password):


    if len(password) < 8:
        return False
    if re.compile('[a-z]+').findall(password) and re.compile('[A-Z]+').findall(password) and re.compile(r'\d+').findall(password):
        print("True")
        return True


print("비밀번호 말해라")
check_password(input())

