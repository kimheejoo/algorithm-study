import sys

'''
N = int(sys.stdin.readline())
arr = {i:int(sys.stdin.readline()) for i in range(1, N+1)} 
visited = [False] * (N+1)
result = []

for i in range(1, N+1):
    tmp = []
    if not visited[i]:
        visited[i] = True
        tmp.append(i)
        while tmp:
            if not visited[arr[tmp[-1]]]:
                visited[arr[tmp[-1]]] = True
                tmp.append(arr[tmp[-1]])
            else:
                if tmp[0] == arr[tmp[-1]]:
                    for j in tmp:
                        result.append(j)
                else:
                    for j in tmp:
                        visited[j] = False
                tmp = []

print(len(result))
for i in sorted(result):
    print(str(i))
'''

def DFS(i, start):
    visited[i] = True

    if not visited[arr[i]]:
        DFS(arr[i],start)
    elif visited[arr[i]] and arr[i] == start:
        result.append(i)


N = int(sys.stdin.readline())
arr = {i:int(sys.stdin.readline()) for i in range(1, N+1)}
result = []

for i in range(1,N+1):
    visited = [False] * (N+1)
    DFS(i,i)

print(len(result))
for i in sorted(result):
    print(i)