# n,m,k,x = map(int,input().split())
# graph = []
# dis = 0
# for i in range(m+1):
#     graph.append(list(map(int,input().split())))
#
#
# def dfs(graph, x, visited):
#     global dis
#     visited[x] = True
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[x]:
#         if dis == k:
#             print(i)
#         if visited[i] ==
#
#         if not visited[i]:
#             dfs(graph, i, visited)


#
# # 각 노드가 방문된 정보를 표현 (1차원 리스트)
# # 여기서는 인덱스 0도 리스트에 존재하기에 9를 곱해주어 초기화해줌
# visited = [False] * (m + 1)
#
# # 정의된 DFS 함수 호출
# dfs(graph, x, visited)


from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)



# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x]) # 큐를 이용해 여기에 데이터 저장함
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)


# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
    check = False
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
            check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)























