money = int(input("투입한 돈 "))
price = int(input("물건 값 "))

change = money - price
print("거스름돈: ", change)
#500으로 나누어서 몫이 500원짜리의 개수
#500으로 나눈 나머지를 계산한다.
#100으로 나누어서 몫이 100원짜리의 개수
coin500s = change // 500
change = change % 500
coin100s = change // 100

print("500원 동전의 개수: ",coin500s)
print("100운 동전의 개수: ", coin100s)