n = input()
list = list(map(int,n))
result = list[0]


#  이건 모험가 길드 문제와 달리 리스트 안에 값과 진행 변수 비교가 아니고
#  누적해서 더하는 거라서 len(list)가 더 적합한건가????
for i in range(1,len(list)):
    if list[i] <= 1 or result <= 1:
        result = result + list[i]
    else:
        result = result * list[i]



print(result)