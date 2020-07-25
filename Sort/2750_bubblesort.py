#정렬
n = int(input())
num = [int(input()) for _ in range(n)]

for i in range(len(num)) : 
    for j in range(len(num)) : 
        if num[i] < num[j] : 
            num[i], num[j] = num[j], num[i]
            
for n in num : 
    print(n)
