import sys

N, D = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    s, e, leng = map(int, sys.stdin.readline().split())
    if e <= D:
        arr.append([s,e,leng])

distance = [i for i in range(D+1)]

for i in range(D+1):
    if i:
        distance[i] = min(distance[i], distance[i-1]+1)
    for j in arr:
        if j[0] == i:
            distance[j[1]] = min(distance[j[0]]+j[2], distance[j[1]])
    print(distance)

print(distance[-1])