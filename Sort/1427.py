#소트인사이드
#수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

n = list((input())
n.sort(reverse=True)
for i in n:
    print(i,end="")
