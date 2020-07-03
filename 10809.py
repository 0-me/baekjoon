#알파벳 찾기
#문자열 위치 찾기 함수 find
#
s = str(input())
for i in range(ord('a'),ord('z')+1):
    print(s.find(chr(i)), end=" ")
