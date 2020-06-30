#상근날드
#버거와 음료 각각 리스트 생성 후 최소값 구하기
b=[]
d=[]
for i in range(3):
    b.append(int(input()))
for i in range(2):
    d.append(int(input()))
print(min(b)+min(d)-50)
