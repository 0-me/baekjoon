#피보나치 수열
#f(n) = f(n-1) + f(n-2)
#0일때는 0을 1일때는 1을 반환

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))
        
