# n = list(map(str,input()))
# alpa = []
# num = []
# result = 0
#
# for i in range(len(n)):
#     if n[i].isalpha():
#         alpa.append(n[i])
#
#     else:
#         num.append(int(n[i]))
#
#
#
# alpa.sort()
# num.sort() # 리스트 타입임
#
# for k in range(len(alpa)):
#     print(alpa[k],end="")
# print(sum(num))


## 답지 ##

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))



