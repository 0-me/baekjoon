#1. N을 5로 나눔-> 나머지가 0이면 끝 0이 아니면 2번을 실행
#2. N을 5로 나눈 나머지를 3으로 나눔 -> 나머지가 0이면 끝 아니면 3번을 실행
#3. 5로 나눈 값의 몫을 하나 줄이고 다시 3으로 나눔 -> 2번 반복
#삼항연산자 a and b or c == (a and b) or c
#a가 false이면 (a and b)가 false이므로 바로 c를 리턴
#a가 true이고 b도 true이면 c는 확인할 필요가 없으므로 b가 리턴

N = int(input())
five = N // 5
three = 0
N %= 5
 
while five >= 0:
    if N % 3 ==0:
        three = N//3
        N %= 3
        break
    five -= 1
    N +=5
 
print(N==0 and (three+five) or -1)
