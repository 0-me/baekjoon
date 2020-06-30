#별찍기
#첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n = int(input())
for i in range(1,n):
    print("*"*i)
for i in range(n,0,-1):
    print("*"*i)
