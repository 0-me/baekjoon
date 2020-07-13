#소수
#자연수 m,n 사이의 소수들의 합과 최솟값

m = int(input())
n = int(input())
a = []

for i in range(m,n+1):
    if i <= 1:
        pass
    elif i==2:
        a.append(i)
    else:
        for j in range(2,i):
            if i%j ==0:
                break
            elif j==i-1:
                a.append(i)
    
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))
    
