#피보나치 수열
#f(n) = f(n-1) + f(n-2)

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))
        
