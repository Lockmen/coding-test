n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될때 까지 1씩 빼기



    target = (n // k)  * k
    result += (n - target)     # N에서 K의 배수를 빼면 N-1 실행한 횟수가 됨
    n = target                 # 이런식으로 배수 확인 과정에서 N-1 과정도 한꺼번에 계산을 해버리면 효율이 더 높아짐

    # N이 K 보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

