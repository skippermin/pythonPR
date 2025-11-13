myid="skip"
mypasswd="abcde"

#제한회수
count = 5
i=1
#무한반복문 스타일로 만들기
while True:
    if(i>count):
        print("제한횟수 초과!!")
        break
    #1.입력받기
    print("----------%d 번째 ---------------" %(i))
    id = input("id: ")
    passwd = input("PW: ")
    #2.모두 일치하면 반복문 탈출하기
    if(id == myid and passwd == mypasswd):
        print("로그인 성공! ")
        break
    #3. 그렇지 않다면 처음부터 다시!
    else:
        print("id 또는 pw가 틀렸습니다. 다시입력하세요")
    i += 1

###
print("프로그램을 종료합니다.")