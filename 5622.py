word = input().lower()
num = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

time = 0
for i in range(len(word)):
    for j in num:
        if word[i] in j :
            time += num.index(j) +3
print(time)
