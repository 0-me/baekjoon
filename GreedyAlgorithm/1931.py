#회의실 배정
#최대 회의 개수
#끝나는시간을 먼저 기준으로 정렬하고
#시작하는 시간을 정렬한다.

import sys

n = int(sys.stdin.readline())
time = []
cnt = 0
start = 0
for _ in range(n):
    time.append(list(map(int,sys.stdin.readline().split())))
time.sort(key=lambda x: [x[1], x[0]])
for i,j in time:
    if i >= start:
        start = j
        cnt += 1
print(cnt)   
