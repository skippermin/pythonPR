# 두 정수를 인자로 받아서 결과를 리턴하는 더하기함수만들기!
def 더하기(num1, num2):
    # global result
    result = num1 + num2
    return result
#####################
result = 0
# 새로 만들어지는 result는 0 이 들어감 들여쓰기가 안되면 전역 되면 지역 변수 바깥에서 정의한 전역 변수를 쓸려면 global를 붙어줘야 한다.
# 27page를 바꿔야 하는 부분이 발생함
result = 더하기(3,5)
print(result)

result = 더하기(13,3)
print(result)
