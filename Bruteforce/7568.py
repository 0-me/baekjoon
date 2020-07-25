#덩치
#for문으로 사람들의 키와 몸무게를 비교

n = int(input())
people = []         #사람들의 키와 몸무게 전체를 담는 리스트
for i in range(n):
    x, y = map(int, input().split())
    people.append([x,y]) #이차배열 활용
    
for i in range(n):
    rank = 1
    for j in range(n):
        #키와 몸무게가 다 클때만 rank를 1 증가시킴.
        #둘 중 하나라도 작으면 rank는 증가하지 않음.
         if people[j][0] > people[i][0] and people[j][1] > people[i][1]: 
            rank += 1
    print(rank, end =" ")
        
