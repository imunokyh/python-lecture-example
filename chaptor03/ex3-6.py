"""
시험 합격,불합격 판별
"""

pilgi = int(input("필기시험 점수를 입력하세요 : "))
silgi = int(input("실기시험 점수를 입력하세요 : "))

if pilgi >= 80 and silgi >= 80 :
    result = "합격"
else :
    result = "불합격"

print("- 결과 : %s" % result)