#상수, 큰 값 구하기
#[::-1]은 단순하게 문자열을 뒤집어 준다.

a, b = input().split()
a = a[::-1]
b = b[::-1]
print(max(a, b))
