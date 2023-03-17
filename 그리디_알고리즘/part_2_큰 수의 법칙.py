n,m,k = map(int, input().split())
data = list (map(int, input().split()))


data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰수

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1

  if m == 0:
    break

  result+=second # 두 번째로 큰 수를 한 번 더하기
  m -= 1

print(result) # 최종 답안 출력









