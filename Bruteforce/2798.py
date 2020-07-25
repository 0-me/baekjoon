#블랙잭
#3개의 카드를 3개의 for문을 이용하여 첫 번째부터 순서대로 탐색

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = len(a)

answer=0
for i in range(0,b-2):
    for j in range(i+1,b-1):
        for k in range(j+1,b):
            num = a[i]+a[j]+a[k]
            if answer < num < m:
                answer = num
            elif num == m:
                answer = num
                break
print(answer)
