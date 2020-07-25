#나이순 정렬
#lambda를 사용해 나이값을 기준으로 정렬

n = int(input())
people = []
for i in range(n):
    people.append(list(map(str,input().split())))
people.sort(key=lambda x: int(x[0]))
for i in people:
    print(i[0],i[1])
