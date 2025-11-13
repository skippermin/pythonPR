p = []
#5명이상 맴버가 속한 아이돌이나 캐릭터의 이름을 입력받아 리스트에 저장하기!

#삼국지
num = 7

for i in range(num):
    #p에 추가한다. 입력받아서 추가.
    #p.append(input("이름: "))
    name=input("이름: ")
    p.append(name)
    print(p)


print("삼국지: ")
print(p)
#sort 정렬 하는 것 안에 아무것도 안 주면 오른차로 정렬
#정렬하기
p.sort()

#index가 가장 중요 엑셀 가장 첫번째 인덱스는 0을 이용한다. 리스트 항목이든 어떠한 데이터든 여러개의 데이터를 저장할 때 쓰느 맨 앞에 있는 것은 0이다.
for i in range(len(p)):
    print("맴버", i,":",p[i])
