from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        graph[x][y] = 0
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

#  모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치가 이번에 1로 방문 처리 되는 거라면(True) reulst 값을 증가시켜준다.
        # 이번이 아닌 이전에 1로 처리 된거라면(True) result 값은 증가시키지 않는다.
        if dfs(i , j) == True:
            result += 1

print(result)






