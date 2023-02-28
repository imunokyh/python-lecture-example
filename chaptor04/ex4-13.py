"""
영문장의 모음 개수 구하기
"""

s = "Love me, love my dog."

i = 0
count = 0

print("문장:", s)  
print("모음 : ", end = "")

while i <= len(s) - 1 :
    if (s[i] == "a" or s[i] == "A"  or s[i] == "e" or s[i] == "E" \
        or  s[i] == "i" or s[i] == "I" or s[i] == "o" or s[i] == "O" \
        or s[i] == "u" or s[i] == "U") :
        count += 1
        print(s[i], end=" ")
        
    i += 1
   
print("\n모음의 개수 :", count)