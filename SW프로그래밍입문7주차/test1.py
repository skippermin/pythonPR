#
while (True):
    # 정수 N을 입력받습니다.
    N = int(input())
    # 정수 N이 3이상이거나 20이하이면 반복문을 탈출하고
    # 그렇지 않으면 다시 입력받도록 반복문을 완성하세요
    if (N >= 3 and 20 >= N):
        break
    else:
        print("다시입력하세요")

# N부터 숫자를 하나씩 감소시켜 출력하는 반복문을 완성하세요
for i in range(N, 1, -1):
    print(i, end=',')

print("1 찾는다!")

num = int(input(""))

if(num %7==0) :
    if(num>=1000 and num<2000) : print("I Love It!")
    elif(num<1000) : print("I Like It!")
    else : print("!")
else : print("!")

#힌트 : 정수를 입력받아서 조건에 따라 출력문을 작성합니다.
n = int(input())

if(1000 >=n ) and (n < 3000): print("I Like It!")
elif(n >= 1000) or (n < 2000): print("I Love It!")
else: print("!")
#입력안내용 메시지는 작성하지 않습니다.