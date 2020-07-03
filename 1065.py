#한수

n = int(input())
han = 0
for i in range(1, n+1):
    if i < 100:
        han +=1
    else:
        l = list(map(int, str(i)))
        if l[0] - l[1] == l[1] - l[2]:
            han += 1
print(han)
