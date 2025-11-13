score = int(input("과목 점수를 입력하세요: "))
# 학점 구간은 A,B,C,D,F
# +- 기준은 자유
# 일의 자리는 어떻게 해야 하지
if (score >= 90) : grade = "A"
elif (score >= 80) : grade = "B"
elif (score >= 70) : grade = "C"
elif (score >= 60) : grade = "D"
else: grade = "F"

# 전제조건 score >= 60 인 경우에만 쌍 이프 switch 문 사용은...

# +, 0을 붙입니다.
if(score >= 60):
 if(score % 10 >= 5 or score == 100) : grade += '+'
 else: grade += '0'

#
#
print("학점은" + " " + grade + " " + "입니다. ")
