#스택수열

n = int(input())  #입력받은 n
stack = []        
op = []           #push(+), pop(-) 연산자 표시
cnt = 1           
temp = True

for i in range(n):
    num = int(input())    
    while cnt <= num:       #cnt와 num이 같을때 까지 
        stack.append(cnt)   #stack에 cnt를 추가
        op.append('+')      #push 연산자 표시 추가
        cnt += 1 
    if stack[-1] == num:    #stack에 저장된 마지막 수와 num이 같다면
        stack.pop()         #stack에서 pop
        op.append('-')      #pop 연산자 표시 추가
    else:
        temp = False        #그게 아니라면 상태를 False로 변경
if temp == False:
    print('NO')           
else:
    for i in op:
        print(i)            #연산자 출력
        
