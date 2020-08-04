#제로
#입력이 0이 아니면 스택에 추가
#입력이 0이면 제일 마지막에 추가한 수를 스택에서 제거

#마지막으로 스택에 들어있는 수들의 합을 출력한다.

#함수로 정의해서 구현한 경우
def push(x):
    s.append(x)

def pop():
    s.pop()

K = int(input())
s = []

for _ in range(K):
    num = int(input())
    pop() if num == 0 else push(num)
    
print(sum(s))


#함수를 정의하지않고 구현한 경우
n = int(input())
s = []
for i in range(n):
    num = int(input())
    if num == 0:
        s.pop()
    else:
        s.append(num)
print(sum(s))
