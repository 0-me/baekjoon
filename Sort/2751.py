#수 정렬하기2
#2750과 유사하지만 N의 개수가 1,000,000개 까지 주어진다.
#2750과 유사하게 풀었더니 시간초과가 나타났다.
#효율적으로 입력을 받기위해 input() 대신 sys,stdin.readline()을 사용한다.
#마찬가지로 출력은 sys.stdout.write을 사용한다.

import sys

n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')
