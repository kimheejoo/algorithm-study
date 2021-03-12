import sys
from collections import deque

def BFS(i, j):
    x = [1, 1, 1, 0, 0, -1, -1, -1]
    y = [1, 0, -1, 1, -1, 1, 0, -1]

    queue = deque()
    queue.append((i,j))

    while queue:
        now = queue.popleft()
        for i in range(8):
            next_x = now[0] + x[i]
            next_y = now[1] + y[i]
            
            if (0 <= next_x < h) and (0 <= next_y < w):
                if arr[next_x][next_y] == 1:
                    arr[next_x][next_y] = 0
                    queue.append((next_x, next_y)) 

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w * h == 0:
        break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                arr[i][j] = 0
                BFS(i,j)
    print(cnt)