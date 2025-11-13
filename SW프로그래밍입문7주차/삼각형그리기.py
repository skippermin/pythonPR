#삼각형을 *모양으로 출력하자!
# 1. 가로와 세로 입력 받기

w = int(input("가로: "))
h = int(input("세로: "))

#2 힌트: 반복문안에 반복문 쓰기
for i in range(h):
#가로찍기
    for k in range(i+1):
        print("*", end="") #기본으로 출력하는 엔터대신:
    #한줄 내려주기 들여쓰기 -> 한줄 내려줘서
    print()
print("-"*40)
# 왼쪽 직각
for k in range(h,0,-1):
#가로찍
    for i in range(k+1):
     if(i%2 ==0):print("★", end="")
     else: print("☆", end="") #기본으로 출력하는 엔터대신:
    #한줄 내려주기 들여쓰기 -> 한줄 내려줘서
    print()