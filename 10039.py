#5명의 평균점수 구하기
#리스트의 합  sum(리스트명)
score=[]
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    score.append(a)
    
print(sum(score)//5)
