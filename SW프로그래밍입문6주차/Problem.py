#구구단 중 9단만 출력하기
# dan = 9
# 짝수 홀수 합의 구할 때 쓰는 [1, 10, 1], [1, 10, 2]
for i in range(5):
    #무조건 한줄을 내리지 않도록
    print("%d: "%i, end=" ")
    print("Welcome! ")
    print("="*30)
# range 대신 범위를 [] 안에 넣어준다.
for i in [1,2,3,4,5]:
    print("%d: " % i, end=" ")
    print("Hello!")
    print("=" * 30)

for dan in range(1, 10):
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("%2d * %2d = %2d "%(i, dan, dan*i), end=" ")
    print("="*30)

print(" 출력 완료 하였습니다.")
