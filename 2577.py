#str함수: 문자열로 변환
#그 후 count를 사용하여 그 리스트에 문자가 몇 개씩 있는지 print해준다.

a = int(input())
b = int(input())
c = int(input())

num = list(str(a * b * c))
for i in range(10):
    print(num.count(str(i)))
