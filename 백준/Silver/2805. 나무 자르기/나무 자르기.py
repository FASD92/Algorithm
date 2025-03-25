import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = 0
highest = arr[-1]
best_h = 0

while start <= highest:
    h = (start + highest) // 2
    cutted = sum(x - h for x in arr if x > h)

    if cutted >= M:
        best_h = h
        start = h + 1
    else:
        highest = h - 1

print(best_h)