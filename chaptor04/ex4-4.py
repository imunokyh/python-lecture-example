"""
1에서 10까지 누적 합계 출력
"""

sum = 0

for i in range(1, 11) :
    sum = sum + i    
    print("i의 값 : %d => 합계 : %d" % (i, sum))
