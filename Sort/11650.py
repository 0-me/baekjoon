#좌표 정렬하기
import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
a.sort(key=lambda x: (x[0],x[1]))
for i in a:
    print(i[0], i[1])
