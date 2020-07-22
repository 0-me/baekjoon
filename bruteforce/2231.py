#분해합
#어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합
#1부터 n까지 전부 계산

n = int(input())
answer = 0
for i in range(1, n+1):
    num = list(map(int, str(i)))
    if(i + sum(num) == n):
        answer = i
        break
print(answer)
