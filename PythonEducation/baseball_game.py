# 컴퓨터가 3자리 숫자를 문제로 내도록.

# 1 ~ 9로만 사용
# 중복된 숫자 허용 X

from random import sample


cpu_numbers = sample(range(1, 10), 3)

print(cpu_numbers)

while True:
    # 숫자 3개를 저장할 공간
    user_numbers = list()

    # 3자리 숫자를 입력하면 -. 3칸의 목록으로 분리
    input_num = int(input('3자리 숫자를 입력: '))
