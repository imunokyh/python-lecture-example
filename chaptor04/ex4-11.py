"""
1부터 10까지 누적 합계
"""

sum = 0
i = 1

while i <= 10 :
    sum += i           # sum = sum + i 와 동일
    print("i의 값 : %d => 합계 : %d" % (i, sum))
    i += 1             # i = i + 1 과 동일