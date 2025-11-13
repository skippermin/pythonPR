items = {"커피음료":100, "펜":200, "종이컵":300, "우유": 400, "콜라":500, "책": 600}

#물건이 잇으면 가격을 보여주고, 없으면 추가하기
#물건이름이 . 이면 종료!
while True:

    name = input("물건이름: ")
    if name ==".": break
    if name in items.keys():
        print(items[name])
    else:
        print("없으므로 이 항목을 추가합니다.")
        price = int(input("가격: "))
        items[name] = price
        print(items)