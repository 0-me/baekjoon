#별찍기-프렉탈
#n은 3의 거듭제곱
#크기 n의 패턴은 n x n 정사각형 모양이다.

def make_star(n):
    stars = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            stars.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            stars.append(n[i % len(n)]* 3)
    return list(stars)
    
star = ["***","* *","***"]
n = int(input())
k = 0

#n의 지수 k 구하기, 반복적으로 n을 3으로 나누어 준다.
while n != 3:
    n = int(n / 3)
    k += 1
    
for i in range(k):
    star = make_star(star)
for i in star:
    print(i)
            
