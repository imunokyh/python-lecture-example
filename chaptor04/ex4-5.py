"""
1에서 100까지 중 5의 배수의 합계 출력
"""

sum = 0

for i in range(1, 101) :
    if i%5 == 0 :
        sum += i             # sum = sum + i와 동일
    
print("1~100 정수 중 5의 배수의 합계 : %d" % sum)
