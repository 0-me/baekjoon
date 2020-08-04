#괄호를 문자열로 입력받아 list로 변환
#시작괄호(가 나오면 cnt에 1을 더해주고, 종료괄호가 나오면 1을 빼준다
#-1이 되면 NO를 출력해주고 for문을 빠져나온다.
#0보다 크다면 NO를 출력해주고
#0이라면 YES를 출력해준다.

n = int(input())
for i in range(n):
    a = list(input())    
    cnt = 0
    
    for j in range(len(a)):
        if cnt < 0:
            break
        
        if a[j] == '(':
            cnt += 1
        elif a[j] == ')':
            cnt -= 1
    if cnt == 0:
        print('YES')
    else:
        print('NO')
        
        
    
