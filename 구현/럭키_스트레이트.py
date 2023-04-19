# 리스트 형이 아니더라도 input() 'str'형으로 n[i] 이런식으로 표현이 가능하구나!!!!!
n = list(map(int,input()))

result = 0
result2 = 0
for i in range(len(n)//2):
    result+=n[i]
    print(result)

for j in range((len(n)//2),len(n)):
    result2+=n[j]
    print(result2)



if result == result2:
    print("LUCKY")
else:
    print("READY")



