import sys

h, w = map(int, sys.stdin.readline().split())

block = list(map(int, sys.stdin.readline().split()))
rain = 0

for i in range(w):
    left_max = max(block[:i+1])
    right_max = max(block[i:])
    point = min(left_max,right_max)
    rain += abs(point - block[i])

print(rain)