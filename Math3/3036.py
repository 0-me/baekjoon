#링
#최대공약수를 구해서 기약 분수로 만든다.

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
n = int(input())
r = list(map(int,input().split()))

for i in range(1,n):
    n = gcd(r[0],r[i])
    print(r[0]//n,"/",r[i]//n,sep='')
