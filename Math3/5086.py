#입력 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.
#각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수면 factor, 배수는 multiple, 둘 다 아니라면 neither를 출력

while True:
    a, b = map(int,input().split())
    if a==0 and b ==0:
        break
    if a%b == 0:
        print('multiple')
    elif b%a ==0:
        print('factor')
    else:
        print('neither')

