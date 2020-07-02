#나머지
#set 집합 순서가 없고, 집합안에서는 unique한 값, mutable 객체
a = []
for i in range(10):
    n = int(input())
    a.append(n % 42)
a = set(a)
print(len(a))
