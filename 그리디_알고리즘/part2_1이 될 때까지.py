n,k = map(int, input().split())


result = []
cnt = 0


if n%k == 0:
    result = n//k
    cnt = cnt + 1

else:
    result = n - 1
    cnt = cnt + 1


while result > 1:
    if result % k == 0:
        result = result // k
        cnt = cnt + 1

    else:
        result = result - 1
        cnt = cnt + 1

print(cnt)













