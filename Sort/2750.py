#정렬
#sorted 정렬함수는 는 어떤 이터러블 객체도 받을 수 있다.
#정렬된 결과는 list로 반환
#기존의 리스트를 변경하는 것이 아니라 정렬된 새로운 리스트를 반환한다.
#내림차순 정렬시 sorted(_____,reverse=True)
#sort()는 리스트 자체를 변경해 버린다

num = sorted([int(input()) for _ in range(int(input()))])
for i in num:
    print(i)
