#가격 세팅: 메뉴와 가격은 자유입니다.
americano_price = 4500
cafelatte_price = 5000
capucino_price = 5500
total_price = 0;

#각 메뉴별로 몇 잔인지 입력 받기
americano = int(input("아메리카노 개수는 "))
cafelatte = int(input("카페라떼 개수는 "))
capucino = int(input("카푸치노 개수는 "))
price = 0 # 총합이라고 한다. 및 파이썬에서는 변수를 만들시 한 번 씩 초기화를 진행해야 한다.

#메뉴 개수 * 메뉴 가격을 구하여 total price에 합산하기
price1 = americano * americano_price
price2 = cafelatte * cafelatte_price
price3 = capucino * capucino_price
total_price = price1 + price2 + price3
print("아메리카노는 ", price1, "원 입니다. ")
print("카페라떼는", price2, "원 입니다. ")
print("카푸치노는", price3, "원 입니다. ")
print("총", total_price, "원 입니다. ")
