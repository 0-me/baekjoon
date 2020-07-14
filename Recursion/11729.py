#하노이 탑
#n개의 원판이 있을 때, n-1개의 원판을 1번에서 2번으로 옮긴 뒤
#가장 아래에 있는 원판을 1번에서 3번으로 옮긴다.
#그리고 n-2개의 원판을 2번에서 3번으로 옮긴다.

n = int(input())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)
