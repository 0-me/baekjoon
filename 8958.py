n = int(input())
for i in range(n):
    a = input()
    b = list(a)
    sum = 0
    c = 1
    for i in b:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)    
