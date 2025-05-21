"""
2차원 배열 dots
dots[i][j] = 1 or 0

base case
모든 칸이 0 또는 1이면 return 0 or 1

반복문으로 기준점, 예를 들어 (0,0)과 값이 같은지 check 하다가
기준점이 0이면 return 0
기준점이 1이면 return 1하는 로직


중간에 기준점과 다른 dot을 발견하면 바로 return
그리고 dots를 4등분해서 재귀

"""
import sys

N = int(input())

#print(N)
dots = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
#print(dots[0][0])

def is_same(x, y, size):
    base = dots[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if base != dots[i][j]:
                return False
    return True

def quad(x, y, size):
    if is_same(x, y, size):
        print(dots[x][y], end='')
        return
    half = size // 2
    print('(', end='')
    quad(x, y, half)
    quad(x, y + half, half)
    quad(x + half, y, half)
    quad(x + half, y + half, half)
    print(')', end='')

quad(0, 0, N)