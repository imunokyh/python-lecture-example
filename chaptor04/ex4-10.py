"""
구구단 2단 ~ 9단 출력
"""

print("-" * 50)

for a in range(2, 10) :         # 2단 ~ 9단
    for b in range(1, 10) :
        print("%d x %d = %d" % (a, b, a*b))
           
    print("-" * 50)