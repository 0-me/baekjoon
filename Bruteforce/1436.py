#영화감독 숌
#666을 포함하는 n번째 숫자 찾기
#666부터 확인, 1씩 증가시키며 in 함수를 이용해 문자열 내에 666이 포함되어 있는지 확인한다.

n = int(input())
count = 0
six = 666
while True:
    if '666' in str(six):
        count += 1
    if count ==n:
        print(six)
        break
    six += 1

        
