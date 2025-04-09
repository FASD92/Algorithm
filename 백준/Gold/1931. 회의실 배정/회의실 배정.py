"""
회의 개수 N
회의 I에 대해 시작시간, 끝나는 시간
각 회의가 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수 -> 그리디 알고리즘 적용

회의의 시작시간과 끝나는 시간이 같을 수는 있음
->이 경우에는 시작하자마자 끝나는 것

첫째줄 회의의 수 N
둘째줄부터 N+1, 각 회의의 정보(시작, 종료시간)

각 회의의 시작과 종료시간을 담긴 튜플 리스트 선언 meetings
종료 시간 기준으로 정렬, 종료 시간 같을 시 시작 시간으로 정렬
람다 써야됨

배정한 회의 수 count = 0으로 선언 및 초기화

마지막으로 배정한 회의의 종료 시간 last_end = 0으로 선언 및 초기화

for문으로 회의들을 하나씩 반복하는데 반복 인자는 start, end

만약 현재 선택한 회의의 시작시간이 마지막으로 배정한 회의의 종료 시간 이후라면
count에 +=1을 하고 현재 회의의 종료 시간을 last_end에 업데이트한다
즉, '배정한다.'
"""
n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0

for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)