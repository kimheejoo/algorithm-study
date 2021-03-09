import sys

N = int(sys.stdin.readline())
line = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    line.append((x, y))
line.sort(key=lambda x:x[0])

# 현재를 기준으로 그려진 선의 시작점(선의 시작)과 끝점(선의 끝)
s = line[0][0]
e = line[0][1]

result = e - s

for i in range(1, N):
    if line[i][0] <= e and line[i][1] <= e: # 현재 그은 선이 전에 그은 선에 완전히 겹칠때
        continue

    if line[i][0] <= e <= line[i][1]: # 일부만 겹칠때, 겹친부분 빼주기
        result += (line[i][1]-line[i][0]) -(e - line[i][0])
        e = line[i][1]
        s = line[i-1][0]
    else:
        result += line[i][1]-line[i][0]
        e = line[i][1]
        s = line[i][0]

print(result)