#직사각형에서 탈출
#경계선까지의 거리가 대각선이 최소인 경우는 없다는 것이 포인트
# x, y와 x, y좌표를 기준으로 w, h까지의 거리를 고려해야한다.

x, y, w, h = list(map(int, input().split()))
print(min(x, y, w - x, h - y))
