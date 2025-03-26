"""
막대기 개수 N
막대기 높이들을 입력을 int 맵핑으로 리스트 생성 bars
오름차순으로 남아버린 것들을 위한 처리용으로 0 추가
막대기를 오름차순으로 정렬할 스택 생성 stk
막대 너비를 계산할 width 선언 => 이건 반복할 때마다 생성해도 될 듯?
넓이를 저장할 area 선언 => 이거도?
가장 넓은 넓이를 저장할 max_area
pop한 막대의 높이를 저장할 height => 이거도 반복할 때마다...?!


N번만큼 반복문
i==0일 때는 bars[i]를 그냥 stk에 집어넣음

i>=1일 때
    bars[i]를 stk[-1]과 비교함
    bars[i]>=stk[-1]일 경우에는 stk.append()
    return

    bars[i]<stk[-1]일 경우에는
    height = stk.pop()
    if not stack:
        width = i
    else:
        width = i - stk[-1] - 1
    area = height * width
    if area > max_area:
        max_area = area

    모든 반복이 끝나면 max_area를 return 
"""
import sys

while True:
    readline = list(map(int,(sys.stdin.readline().strip().split())))
    if readline[0] == 0:
        break

    N = readline[0]
    bars = readline[1:]
    bars.append(0)

    stk = []
    max_area = 0
    i = 0
    
    while i < len(bars):
        if not stk or bars[i] >= bars[stk[-1]]: # 만약 stk이 비어있거나 현재 막대기가 stk 맨 위에 있는 막대기보다 크거나 같을 때(즉 오름차순일 때)
            stk.append(i)   # stk에 인덱스를 추가함
            i += 1
        else:   # stk의 오름차순이 멈췄을 때
            height = bars[stk.pop()]  # pop한 걸 height로 저장함
            if not stk:
                width = i
            else:
                width = i - stk[-1] - 1
            area = height * width
            max_area = max(max_area, area)

    print(max_area)