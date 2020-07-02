#별찍기
#공백 0 1 2 3 4 3 2 1 0
#별 개수 2n-1

n= int(input())
for i in range(n):
    print(' '*i+'*'*(2*(n-i)-1))
for i in range(2,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
