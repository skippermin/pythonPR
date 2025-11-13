#정기예금 금리계산기를 만들어보시지요.
#추후에 한국어로 된 거 영어로 바꿔서 계산하세요.
money = int(input("얼마를 저축하시겠습니까?: "))
rate = float(input("은행의 저축이율은 얼마입니까?(%): "))
기간 = int(input("예금기간은 몇 년인가요?(년) : "))
이자 = money * rate /100 * 기간

# score = 10
# score += 1
# score = score + 1
# print(score)


이자과세 = 이자 * 15.4/100
money+=이자-이자과세
print("         세전이자: ", 이자)
print("이자과세(이자의 15.4%): ", 이자과세)
print("         세후이자 ", 이자-이자과세)
print(기간, "년 후 받을 금액은 ", money, "입니다.")