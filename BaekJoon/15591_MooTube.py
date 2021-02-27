import sys

# graph = [정점 번호, 거리]
def search(k, node):
    result = 0
    visited = [False] * (len(graph.keys())+1)
    stack = graph[node][:]
    visited[node] = True

    # 정점과 인접해있는 노드에서 k이상이면 result++
    for s in stack: 
        visited[s[0]] = True
        if s[1] >= k:
            result += 1

    # 인접해있는 노드말고
    while stack:
        n, d = stack.pop()
        for i in graph[n]:
            if not visited[i[0]]:
                visited[i[0]] = True
                min_d = min(d, i[1])
                stack.append([i[0], min_d])
                if min_d >= k:
                    result += 1
    return result

n, q = map(int, sys.stdin.readline().split())
graph = {i+1: list() for i in range(n)}

for i in range(n-1):
    s, e, distance = map(int, sys.stdin.readline().split())
    graph[s].append([e, distance])
    graph[e].append([s, distance])

for _ in range(q):
    k, node = map(int, sys.stdin.readline().split())
    print(search(k, node))