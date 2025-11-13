#짱구의 친구들
l = ["미미","짱구","훈이","수지","맹구"]
print(l)
#짱구의 친구가 아닌 "미미" 지우고 유리로 바꾸기
#짱구친구 "수지","철수","채송화선생님... 등 추가하기
l[0] = "유리"
print(l)
#짱구친구 "철수", 관련인물 "치타" 추가하기
l.append("철수")
print(l)

l.sort()
print(l)

#짱아 끼워넣기
l.insert(4, "짱아")
print(l)

#아무이름 막 넣어놓고 정렬하기
l.insert(2, "안경태")
l.insert(3, "영심이")
l.insert(4, "유비")
print(l)
print(len(l))

##지우기!
#입력을 받아서, 있으면 지우고, 없으면 추가하고
while True:
    name = input("지울이름:")
    if name in l:
        print(name+"있음")
        l.remove(name)
    else:
        print(name+"없음")
        l.append(name)
    print(l)