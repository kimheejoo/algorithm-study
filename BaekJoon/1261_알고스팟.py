import sys
import heapq

M, N = map(int, sys.stdin.readline().split())
arr = []
queue = []
result = [sys.maxsize] * (M*N)
direction = [[-1,0], [0,1], [1,0], [0,-1]] #위, 오, 아래, 왼

result[0] = 0
heapq.heappush(queue, [0,0]) # 좌푯값[x,y]

for i in range(N):
    tmp = []
    line = map(int, sys.stdin.readline().rstrip())
    for j in line:
        tmp.append(j)
    arr.append(tmp)

while queue:
    x, y = heapq.heappop(queue)
    for i in direction:
        if 0 <= x+i[0] < N and  0 <= y+i[1] < M:
            new_x = x+i[0]
            new_y = y+i[1]
            if result[new_x * M + new_y] > result[x * M + y] + arr[new_x][new_y]:
                result[new_x * M + new_y] = result[x * M + y] + arr[new_x][new_y]
                heapq.heappush(queue, [new_x, new_y])

print(result[-1])