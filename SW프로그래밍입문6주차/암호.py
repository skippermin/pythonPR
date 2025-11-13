#1 id와 pw를 입력받는다.
#2 올바른id와 올바른 pw와 같은지 비교한다.
#3 둘다 같아야 종료, 둘중 하나라도 틀리면 1부터 반복한다.
id = "skipper"
passwd = "12345"

while (passwd != "12345") and (id != "skipper"):
    passwd = input("암호를 입력하시오: ")

print("로그인 성공")