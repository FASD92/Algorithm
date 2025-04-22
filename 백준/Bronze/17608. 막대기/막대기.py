import sys

N = int(sys.stdin.readline())
bars = [int(sys.stdin.readline()) for _ in range(N)]

count = 1  # 마지막 막대기는 무조건 보임
standard = bars[-1]

for i in range(N - 2, -1, -1):  # 오른쪽에서 왼쪽으로
    if bars[i] > standard:
        count += 1
        standard = bars[i]

print(count)