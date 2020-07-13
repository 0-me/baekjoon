#직각삼각형
#가장 큰 수를 제외하고 나머지 작은 숫자들의 제곱의 합과 비교
while(True):
    a = list(map(int, input().split()))
    max_num = max(a)
    if sum(a) == 0:
        break
    
    a.remove(max_num)
    if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
        print('right')
    else:
        print('wrong')
