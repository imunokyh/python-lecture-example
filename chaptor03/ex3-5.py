"""
짝수,홀수 판별
"""

n = int(input("숫자를 입력해 주세요 : "))

if n % 2 == 0 :
    print("%d은(는) 짝수입니다." % n)    
else :
    print("%d은(는) 홀수입니다." % n)