#네번째 점
#리스트 함수 count를 이용해 요소의 개수가 1개인 것을 출력

x_list =[]
y_list =[]

for i in range(3):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]
        
print(x,y)
