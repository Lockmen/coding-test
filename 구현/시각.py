# 확인 데이터가 100만 이하일 때는 이렇게 완전탐색 기법을 사용하는 것도 괜찮다.
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # ex) 03시 20분 35일 때 '032035'를 만들어서 '3'이 '032035'에 포함되는지 여부를 체크한다.
            # 대충 뭔말인지는 알겠는데 내가 손으로 어떻게 풀어야 할지 모르겟네
            if '3' in str(i) + str(j) + str(k):
                print(count)
                count += 1

print(count)
