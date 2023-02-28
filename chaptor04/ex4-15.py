"""
1부터 100까지 누적 합계 출력
"""

i = 1
sum = 0

while True :
    if i > 100 :
        break

    print(i)
    
    sum += i   
    i += 1

print("합계 :", sum)