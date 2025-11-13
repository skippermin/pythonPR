#사각형을 *모양으로 출력하자!
# 1. 가로와 세로 입력 받기

w = int(input("가로: "))
h = int(input("세로: "))

#2 힌트: 반복문안에 반복문 쓰기
for k in range(h):
#가로찍기
    for i in range(w):
        print("*", end="") #기본으로 출력하는 엔터대신:
    #한줄 내려주기
    print()
