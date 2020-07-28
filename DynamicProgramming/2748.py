#피보나치 수2
#10870과 동일하게 함수를 정의해서 푸는 경우 시간초과가 나타난다.

n = int(input())
a=0
b=1
for i in range(n):
    a, b = b, a+b
print(a)
