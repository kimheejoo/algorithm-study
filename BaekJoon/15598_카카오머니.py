import sys
from math import gcd

N = int(sys.stdin.readline())

wallet = 0
charge = None # 충전금
min_M = pow(10,18)

for _ in range(N):
    money , remain = map(int, sys.stdin.readline().split())
    if wallet + money < 0: #충전
        if remain != 0:
            min_M = min(min_M, remain) # min_M(남은 금액의 최소)이 충전금보다 많으면 오버해서 충전한거
        
        charge_tmp = remain - money - wallet #현재 충전된 금액

        #charge -> 충전값 정함
        if charge == None:
            charge = charge_tmp
        else:
            charge = gcd(charge, charge_tmp)
        
        #오버해서 충전했거나, charge==1일때는 무조건 remain이 0이어야하는데 그 조건을 만족 못 시킬 경우
        if (min_M != pow(10,18) and charge <= min_M) or (charge == 1 and remain!=0):
            print(-1)
            break
    else: #충전안해도 될 때는 원래 있던 돈(wallet)과 현재 입출금된 돈(money)를 더하면 현재 남아있는 돈(remain)이 되어야한다.
        if wallet + money != remain:
            print(-1)
            break
    wallet = remain #현재 남아있는 돈(remain)을 원래있던 돈(wallet)에 넣는다.
else:
    if charge == None: #충전금이 사용되지 않을때
        print(1)
    else: print(charge)