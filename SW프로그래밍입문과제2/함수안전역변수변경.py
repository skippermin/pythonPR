a=1
b=2
c=3

def test():
    c=30
    d=100
    global e
    e=1000
    print("test함수에서")
    print("b:%d c:%d d:%d e:%d"%(b,c,d,e))
print("메인에서 함수에서")
print("a = ", a)
print("b = ", b)
print("c = ", c)
#print("d = ", e) 함수에서 정의한 d 변수는 인식불가 error
#print("e = ", e) test가 아직 호출 되기 전이므로 e 변수는 만들어 지기 전이라 error

print("="*50)
b=200
test()
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("e = ", e)