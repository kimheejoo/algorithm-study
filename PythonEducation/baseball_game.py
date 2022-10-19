# 컴퓨터가 3자리 숫자를 문제로 내도록.

# 1 ~ 9로만 사용
# 중복된 숫자 허용 X

from random import sample


cpu_numbers = sample(range(1, 10), 3)

print(f'정답: {cpu_numbers}')

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

    # ?S ?B 인지 판단 -> 힌트 제공
    s_cnt = 0
    b_cnt = 0

    for user_idx, user_val in enumerate(user_numbers):
        for com_idx, com_val in enumerate(cpu_numbers):
            if user_val == com_val:
                if user_idx == com_idx:
                    s_cnt += 1
                else: b_cnt += 1


    # S/B 판정 출력
    print(f'{s_cnt}S{b_cnt}B')
    # 3S가 되었다면? -> 정답 맞춤! -> 게임 종료!
    if s_cnt == 3:
        break

print('추가뿌!!')