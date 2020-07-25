#좌표 정렬하기2
#n개의 좌표를 리스트 형태로 받는다.
#y[1]에 대해 정렬한 후 [0]를 정렬하기때문에 lambda를 사용해준다.

import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
a.sort(key=lambda x: (x[1],x[0]))
for i in a:
    print(i[0], i[1])
