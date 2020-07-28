#python itertools 활용
#itertools.permutations(chars, 2)  # 순열
#c = itertools.combinations(chars, 2)  # 조합

from itertools import permutations

n,m = map(int,input().split())
p= permutations(range(1,n+1), m) # iter(tuple)

for i in p:
    print(' '.join(map(str,i))) # tuple -> str
