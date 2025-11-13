#사칙연산을 함수로~!
#사각형, 삼각형 그리기를 함수로~!
def menubar():
    print("="*50)
    print("1. 두수 입력받기 2. 더하기 3. 빼기 4. 곱하기 5. 나누기, 6 삼각형그리기 0. 종료하기")
    print("="*50)

def plus(x,y):
    print("더하기 함수입니다.")
    print("%d + %d = %d"%(x,y,x+y))
    return (x+y)

def minus(x,y):
    print("빼기 함수입니다.!")
    print("%d - %d = %d"%(x,y,x-y))
    return x-y

def mult(x,y):
    print("곱하기 함수입니다.")
    print("%d * %d = %d"%(x,y,x*y))
    return (x * y)
#y가 0이면 나눗셈 불가처리하기!
def divide(x,y):
    if y==0:
        print("나눗셈 불가!")
        return
    print("나누기 함수입니다.")
    print("%d // %d = %d"%(x,y,x//y))
    return x//y
def mod(x,y):
    if(y==0):
        print("0으로 나눌 수 없습니다")
        return 0
    print("%d %% %d" %(x,y),end="")
    return x%y
def 삼각형그리기(높이):
    for i in range(높이):
        print("*"*(i+1))
#################################
#메인코드를 작성하는 영역!
#필요한 변수를 만들고 초기화!
menu = 0
x=0
y=0
result=0

while True:
    menubar()
    print("현재 x:%d y:%d result:%d"%(x,y,result))
    menu = int(input("메뉴를 입력하세요: "))

    if menu == 0 : break
    elif menu == 1 :
        x = int(input("정수1을 입력하새요: "))
        y=  int(input("정수2을 입력하세요: "))

    elif menu == 2 : result = plus(x,y)
    elif menu == 3 : result = minus(x,y)
    elif menu == 4 : result = mult(x,y)
    elif menu == 5 : result = divide(x,y)
    elif menu == 6 : 삼각형그리기(x)
    if (menu>=2 and menu <=5): print("계산 결과: ", result)

print("프로그램을 종료합니다. ")









