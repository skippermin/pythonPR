#친구이름과 전화번호 5개만 저장하기: 딕셔너리 연습
fr= {}
for i in range(5):
    name=input("이름: ")
    no=input("전화번호: ")
    fr[name] = no
    print(fr)

fr = {"짱구":111, "미미":222, "흰둥이":333}

#key정보보기
print(fr.keys())

#value정보 보기
print(fr.values())

#짱구의 value는 무엇인가?
print(fr["짱구"])

#짱구의 value? 없으므로 에러!
#print(fr["짱아"])

if "짱아" in fr.keys():
    print("짱아있음!")
    print(fr["짱아"])
else:
    print("짱아없음!")

# if "짱아" not in fr.key() :
# print("짱아없음")
# else:
# print("짱아있음")
# print(fr["짱아"])