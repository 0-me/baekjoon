#ATM
#n명의 사람과 돈을 인출하는 최소시간
n = int(input())
time =list(map(int,input().split()))
total = 0
time.sort()   #오름차순으로 시간을 정렬
for i in range(n):
    total += sum(time[:i+1])   #누적합계 계산
print(total)
           
