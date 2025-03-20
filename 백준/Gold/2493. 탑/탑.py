import sys
N = int(sys.stdin.readline().strip())
result = []
tops = list(map(int, sys.stdin.readline().strip().split()))

stack = []  # (인덱스, 높이) 쌍을 저장

for i in range(N):
    # 스택에서 현재 탑보다 낮은 탑 제거
    while stack and stack[-1][1] < tops[i]:
        stack.pop()
    # i == 0 또는 스택이 비었을 때
    if i == 0 or not stack:
        result.append(0)
    else:
        # 스택의 가장 위 탑이 현재 탑보다 높음
        result.append(stack[-1][0])
    stack.append((i + 1, tops[i]))

print(*result)