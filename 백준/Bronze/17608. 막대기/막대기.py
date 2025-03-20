"""
왼쪽부터 차례대로 번호를 붙인 막대들
오른쪽에서 막대가 몇 개가 보이는지?
참고로 맨 오른쪽도 포함임

첫번째 줄은 막대기의 개수를 나타내는 정수 N이니까 int로 변환하고
두번째 줄부터는 readlines().strip()과 int형 맵핑을 통해 리스트 sticks를 선언하고
for문 range(N)만큼 돌려서 만약 sticks[N-1]보다 큰 값을 발견하면 highest라는 int형 변수에 저장
그리고 그보다 더 큰 값을 발견하면 highest를 업데이트함
업데이트 할 때마다 막대기가 보이는 개수를 뜻하는 int형의 변수 count +=1을 함

print 할 때는 count+1로 출력할 건데 왜냐면 오른쪽 막대기는 무조건 보이기 때문임
"""

import sys
count = 0

N = int(sys.stdin.readline().strip())
sticks = []

for i in range(N):
    sticks.append(int(sys.stdin.readline().strip()))

highest = sticks[N-1]

for j in range(N-2, -1, -1):
    if sticks[j] > highest:
        highest = sticks[j]
        count += 1

print(count+1)