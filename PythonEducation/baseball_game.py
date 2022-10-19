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

    # ex. 123 -> [1, 2, 3]으로 분리.
    # 3자리 정수가 들어왔다고 전제하자.

    # 제일 먼저 추가: 백의 자리
    # 그 다음: 십의 자리
    # 마지막: 일의 자리

    user_numbers.append(input_num // 100)
    user_numbers.append((input_num // 10) % 10)
    user_numbers.append(input_num % 10)

    print(user_numbers)