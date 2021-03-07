import sys

def get_max(arr):
    result = 0
    for i in range(0, len(arr), 2):
        if i < len(arr)-1:
            result += arr[i] * arr[i+1]
        else:
            result += arr[i]
    return result

N = int(sys.stdin.readline())
positive = [] #1초과
negative = [] #0이하, 0은 음수가 하나일 때, 곱해지는게 이득
one = [] #1은 곱해지지않고 더해져야 더 큰 수가 나옴

for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp <= 0: negative.append(tmp)
    elif tmp > 1: positive.append(tmp)
    else : one.append(tmp)

negative.sort() # 작은 것부터 나열해서 곱하면 제일 커지는 방향
positive.sort(reverse=True) # 큰 것부터 나열해야 제일 커지는 방향

result = get_max(negative) + get_max(positive) + sum(one) # 1은 모두 더해줘야 제일 커짐

print(result)