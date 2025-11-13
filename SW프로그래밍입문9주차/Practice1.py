def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        print(i, end =" + ")
        sum+=i
    return sum

def get_mult(start, end):

    mult = 1

    for i in range(start, end+1):
        if(i==end): print(i, end=" = ")
        else: print(i, end=" * ")
        mult*=i
    return mult

##########################################
#메인코드를 작성하는 영역!

result = get_sum(1, 10)
print(result)

print("-"*50)

result2 = get_mult(1, 10)
print(result2)