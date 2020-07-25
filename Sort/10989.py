#수 정렬하기3

#0이 10000개 있는 리스트를 선언합니다.
#숫자의 개수를 해당 숫자와 일치하는 인덱스에 저장한다.
#입력받은 숫자를 리스트의 인덱스로 사용해서 해당 숫자의 위치에 1씩 더한다.
#마지막 for문에서 리스트의 앞에서부터 값이 있는 숫자들을 출력한다.

import sys

n = int(sys.stdin.readline())
num = [0]*10001

for i in range(n):
    num[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if num[i] > 0:
        sys.stdout.write((str(i)+'\n')*num[i])
