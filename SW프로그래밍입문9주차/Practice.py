def cal_area(radius):
    print("반지름이", radius , "인 원넓이를 구합니다.")
    area = radius**2*3.14
    return area

r = int(input("반지름을 입력하세요: "))
result = cal_area(r)
print(result)