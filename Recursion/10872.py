#팩토리얼
#factorial은 math library에서 math.factorial()로 사용할 수 있지만 재귀로 구현해보자
#from math import factorial
#print(factorial(int(input())))

#0,1의 결과는 1

def fac(num):
    if num <= 1:
        return 1
    else:
        return = num * fac(num-1)

print(fac(int(input())))
