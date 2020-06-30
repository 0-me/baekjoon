#테스트 케이스 개수가 정해져 있지 않다.
#예외처리
try:
    while True:
        a, b = map(int,input().split())
        print(a+b)
except:
    exit()
