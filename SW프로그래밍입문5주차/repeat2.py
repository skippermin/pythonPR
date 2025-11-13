limit = 15
print("%d세 이상만 관람이 가능한 영화입니다."%limit)

age = int(input("나이를 입력하시오: "))

if age >= limit:
    print("이 영활를 보실 수 있습니다.")
    print("재미있게 관람하세요.")
else:
    print("죄송합나다. 영화관람 나이제한으로 인하여 관람이 불가능합니다.")
    print("이 영화를 보실 수 없습니다.")