#N과 M(1)
#자연수 N,M이 주어졌을 때 길이가 M인 순열을 중복없이 모두 구하는 프로그램
#python itertools 활용
#itertools.permutations(  , 2) - 순열
#itertools.combinations( , 2) - 조합

from itertools import permutations

n,m = map(int,input().split())
p= permutations(range(1,n+1), m) # iter(tuple)

for i in p:
    print(' '.join(map(str,i))) # tuple -> str
