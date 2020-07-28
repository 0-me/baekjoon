#잃어버린 괄호
#최소값을 구하기 위해서는 -를 기준으로 괄호를 추가해주면 된다.
#첫번째 원소에서 +를 기준으로 나누어준 뒤 total에 더해주고
#각 원소에 있는 수들은 total에서 빼주면된다.
a = input().split('-')
total = 0
for i in a[0].split('+'):
    total += int(i)
for i in a[1:]:
    for j in i.split('+'):
        total -= int(j)
print(total)
        
    
    
