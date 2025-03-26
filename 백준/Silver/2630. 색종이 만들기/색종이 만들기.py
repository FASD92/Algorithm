"""
한 변의 길이 N
divide라는 변수 선언 1로 초기화
파란색과 흰색을 카운트할 변수 0으로 초기화
각 칸의 정보 담긴 리스트 paper -> int형으로 N번만큼 저장해서 2차원으로 만듦

이중 반복문을 사용해 해당 2차원 정사각형의 색이 모두 같은 색으로 칠해져있는지 확인하는 함수를 만듦 -> is_same_color
인자는 x,y,size로 받음
색이 같은지 검사할 때 기준은 x,y로 인자 받은 걸 이용해 paper[x][y]를 기준으로 함

그리고 fold라는 함수를 만들 건데
인자는 size, x, y를 받고
is_same_color함수를 이용해 만약 해당 2차원 정사각형의 색이 모두 같다면,
paper의 색이 파란색이면 blue_cnt에 1을 더하고
아니면(하얀색이면) white_cnt에 1을 더한다

그리고 재귀 함수를 사용해야 하는데
half = size//2로 반으로 나누고
2차원 정사각형을 좌상단 우상단 좌하단 우하단 네구역으로 나눠서 검사함
"""

import sys
input = sys.stdin.readline

white_cnt = 0
blue_cnt = 0

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def is_same_color(x, y, size):
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                return False
    return True

def fold(size, x, y):
    global white_cnt, blue_cnt

    if is_same_color(x, y, size):
        if paper[x][y] == 1:
            blue_cnt += 1
        else:
            white_cnt += 1
        return

    half = size // 2
    fold(half, x, y)    #   좌상단
    fold(half, x, y + half) #   우상단
    fold(half, x + half, y) #   좌하단
    fold(half, x + half, y + half)  # 우하단

fold(N, 0, 0)

print(white_cnt)
print(blue_cnt)