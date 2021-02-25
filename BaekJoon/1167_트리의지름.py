import sys

def graph(i):
    far = 0
    diameter = 0
    visited = [False] * (v+1)
    visited[i] = True

    stack = tree[i][:]
    for s in stack:
        visited[s[0]] = True
        if s[1] > diameter:
            far = s[0]
            diameter = s[1]

    while stack:
        node, distance = stack.pop()
        for i in tree[node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                stack.append((i[0], distance + i[1]))
                if diameter < distance +i[1]:
                    far = i[0]
                    diameter = distance+i[1]

    return far, diameter
v = int(sys.stdin.readline())
tree = dict()

for i in range(v):
    tmp = list(map(int, sys.stdin.readline().split()))
    tree[tmp[0]] = list()
    for j in range(1, len(tmp)-1, 2):
        tree[tmp[0]].append((tmp[j],tmp[j+1]))
far, _ = graph(1)
print(graph(far)[1])