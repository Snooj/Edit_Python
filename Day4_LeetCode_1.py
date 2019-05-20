# 이메일 주소는 .과 +를 포함한다. .은 그냥 무시한다. +뒤의 문자열들은 모두 무시된다.
# string의 method인 split과 replace를 사용
def emailArray(email_Input):
    txt=email_Input.split("@")
    headFirst=txt[0] ; tail=txt[-1]
    txt2=headFirst.split("+")
    headSecond=txt2[0]
    headThird = headSecond.replace('.','')
    email_Output = headThird + "@" + tail
    return email_Output

print(emailArray("test.email+alex@leetcode.com"))