#균형잡힌 세상

while True:
    s = input()
    if s == '.':
        break
    stack = []
    temp = True
    for i in s:
        if i == '(' or i == '[':      #여는 괄호를 찾았을땐 스택에 여는괄호 그대로 넣어준다.
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:       #닫는 괄호가 먼저 나오면 
                temp = False          #temp를 False로 바꾸고 break
                break
            if stack[-1] == '(':      #스택의 마지막이 자기자신과 짝이 맞는지 검사하고 pop한다
                stack.pop()
            else:
                temp = False
                break
        elif i == ']':
            if len(stack) == 0:
                temp = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                temp = False
                break
    if temp and len(stack)==0:      #stack이 비워져 있거나 temp가 True이면 yes
        print('yes')
    else:
        print('no') 
