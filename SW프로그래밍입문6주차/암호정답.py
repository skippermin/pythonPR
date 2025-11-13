id = "skipper"
pw = "12345"

while True:
    loginid = input("id: ")
    loginpw = input("pw: ")

    if(id == loginid and pw == loginpw) :
        print("축하! 로그인 성공")
        break
    else:
        print("id 또는 pw, 혹은 둘다 올바르지 않습니다.")


print("로그인 성공")