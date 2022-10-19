# 응용문제 7 - 로또 맞춰보기 예제

# 1. 6개의 숫자 입력받기

from audioop import mul
from random import randint, random


my_lotto_numbers = list()

# 6번 숫자를 입력: for

for i in range(6):
    # 정수 입력
    
    while True:
        input_num = int(input(f'{i+1}번째 로또 번호 입력: '))

        # 받아낸 input_num가 제대로 되었다면? 무한반복 종료 -> 다음 숫자 받으러.

        # 반복종료 조건 1. 1~45 이내?
        # 1 <= 입력값 and 입력값 <= 45

        is_range_ok = (1 <= input_num) and (input_num <= 45)

        # 무한 반복 종료 조건 2. 이미 등록한 번호가 아니어야함.
        # 중복인가? 내 로또 번호에 이미, 입력값이 들어있는가?
        # input_num이 my_lotto_num 안에 포함되어 있는가?
        is_duplicated = input_num in my_lotto_numbers

        if is_range_ok and not is_duplicated:
            # 검사 통과 시 무한 반복 종료
            break
        elif is_duplicated:
            # 중복검사에서 탈락
            print('이미 등록된 숫자 입니다.')
        else:
            # 범위 검사 탈락 시 안내 문구
            print('1~45의 값만 입력 가능합니다.')
            # 다시 입력 시킨다 -> 무한반복 유지 -> break X
    my_lotto_numbers.append(input_num)

# 입력한 숫자 목록 확인
print(my_lotto_numbers)

# 숫자 목록을 작은 수 ~ 큰 수로 정렬. (sort)

# bubble sort 구현해보기

# 2개씩 짝지어 비교 -> 순서가 잘못 됐으면 서로 위치 변경 -> 통째로 6번 반복

for idx, val in enumerate(my_lotto_numbers):
    
    #2개씩 뽑아서 비교
    for j in range(5):

        # 순서가 잘못되었나? 앞의 숫자가 더 큰가?
        if my_lotto_numbers[j] > my_lotto_numbers[j+1]:
            # 두 자료의 위치를 변경
            # 두 변수의 위치 바꿔주기
            tmp = my_lotto_numbers[j]
            my_lotto_numbers[j] = my_lotto_numbers[j+1]
            my_lotto_numbers[j+1] = tmp
        
print(my_lotto_numbers)

# 당첨번호 목록
win_number_list = list()

# 6개의 숫자를 뽑자.

for i in range(6):
    # 사용할 수 있는 번호가 나올 때까지 무한 반복
    while True:
        #random.random() => 0.0 ~ 0.9999의 랜덤값 출현
        rand_num = int(random() * 45 + 1)
        if rand_num not in win_number_list:
            win_number_list.append(rand_num)
            break

# print(win_number_list)

# 당첨 번호도 순서대로 정리 - 파이썬 제공 기능 활용
win_number_list.sort()

# 당첨번호 6개 생성 이후, 보너스 번호 하나 추가 생성
# 기존 당첨 번호와 중복되면 안됨.

while True:
    # 1~45의 랜덤을 쉽게 뽑는 방법?
    bonus = randint(1, 45)
    if bonus not in win_number_list:
        break

# 임시 처리: 당첨번호, 보너스 번호를 고정해둬야 테스트 하기 편하다.
win_number_list = [10, 15, 20 , 25, 30, 35]
bonus = 40 # 보너스 번호 고정
print(win_number_list)

print(f'보너스 번호: {bonus}')

cnt = 0

for i in my_lotto_numbers:
    if i in win_number_list:
        cnt += 1

if cnt == 6:
    print('1등~')
elif cnt == 5:
    if bonus in my_lotto_numbers:
        print('2등')
    else: print('3등')
elif cnt == 4:
    print('4등')
elif cnt == 3:
    print('5등')
else: print('꽝....')