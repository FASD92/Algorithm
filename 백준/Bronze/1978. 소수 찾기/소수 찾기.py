"""
자연수가 입력됐을 때 이게 소수인지 어떻게 판단할 수 있을까
소수는 1과 자기 자신만을 약수로 가진 숫자다.
참고로 1은 소수가 아니다.

주어진 입력들을 int형의 deque로 받음.
1 3 5 7 이런 식으로 주어지니 readlines()에서 .strip을 써야할 듯.

count 변수를 int형으로 선언.
첫번째 항목을 꺼내 n으로 선언
popleft()로 맨 앞부터 소거할 건데,
만약 popleft()의 반환값이 1이면 count에 더하지 않는다. => continue?

반복의 range는 deque가 False가 될 때까지(deque나 리스트는 비어있을 때 false를 반납하다고...)
이중 반복문으로 반복 횟수는 2부터 num까지, 만약 deque[j]==1이면 continue
각 항목마다 j로 나눴을 때, 나머지가 0이면, 1과 본인 외에도 약수가 있다는 거니 break로 while문 앞으로.

입력이 1 3 5 7 일 경우
i가 1일 때 첫번째 항목 deq[0]을 확인하는데
1이니까 popleft만 하고 continue로 while문 앞으로 이동하고
2는 소수니까 바로 count를 하나 추가하고 continue
i가 2일 때 두번째 항목 deq[1]을 확인하니 3,
j가 1일 때,3을 2로 나누면 몫이 0이 아니고

j가 2일 때는 range가 끝난 거니까
이 외에는 소수라고 판단
이렇게 deque가 false가 될 때까지 반복하고
count를 프린트 한다.
"""

import sys
import math
from collections import deque

N = int(sys.stdin.readline().strip())
deq = deque(map(int, sys.stdin.readline().strip().split()))

count = 0  

while deq:
    num = deq.popleft()
    if num == 1:
        continue

    if num == 2:
        count += 1
        continue

    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            break
    else:
        count += 1

print(count)