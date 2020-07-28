#동전 0
#동전의 종류 n 가치의 합 k 필요한 동전 개수의 최솟값 구하기
#동전의 값이 큰 것부터 계산

n,k = map(int,input().split())
coin = []
num = 0

for i in range(n):
    coin.append(int(input()))
  
for i in range(n-1,-1,-1): 
    if k == 0:
        break
    if coin[i] > k:
        continue
    //coin[i]의 개수(몫) num에 더하기    
    num += k//coin[i]
    #k에서 coin[i]를 나눈 후 나머지 금액(나머지)
    k %= coin[i]
print(num)
