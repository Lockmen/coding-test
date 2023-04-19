def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



graph = [ # 2차원 인접 리스트로 표현
    # 인덱스 0부터 8번까지 인접한 노드의 정보를 저장
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# 여기서는 인덱스 0도 리스트에 존재하기에 9를 곱해주어 초기화해줌
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)