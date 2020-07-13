#소수 찾기
#소수를 구하는 함수 prime을 정의해서 풀이하기

n = int(input())
num = list(map(int,input().split()))

def prime(s):
    if s == 1:
        return False
    elif s == 2:
        return True
    for i in range(2, s):
        if s % i == 0:
            return False
    return True
count = 0

for i in num:
    if prime(i):
        count += 1
print(count)
        
