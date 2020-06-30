#a,b,c 세 정수 중 두번째로 큰 정수 출력
#리스트 정렬 sorted(a)
a = list(map(int,input().split()))
b = sorted(a)
print(b[1])
