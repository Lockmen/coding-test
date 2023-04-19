# 리스트를 이용해서 큐를 구현 가능하지만 시간 복잡도 상승으로 라이브러리 사용 권장
# 시간 복잡도 O(1)
from collections import deque

# 큐
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순을 바꾸기
print(queue) # 나중에 들어온 원소부터 출력