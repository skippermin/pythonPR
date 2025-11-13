# agelimit = 10
# heightlimit = 110
#
# age = int(input("나이를 입력하세요: "))
# height = int(input("키를 입력하세요: "))


# sunny = True
#sunny = false
# time = 7
import random

time = random.randint(1,24)
sunny = random.choice([True,False])

if(time>=6 and time<9 and sunny==True):
    print("종달새가 노래합니다.")
else:
    print("종달새는 노래할 수 없어요.")
