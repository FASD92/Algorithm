"""
입력 받은 수열 arr
수열을 만들 스택 stk
결과를 출력할 배열 result

1부터 n까지 추가할 i
arr의 인덱스가 되어줄 idx

"""
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.read().split()))

stk = []
result = []

i = 1
idx = 0

while True:  
    if i <= n:  # 만약 i가 아직 n보다 작거나 같으면
        stk.append(i)   # 일단 그냥 스택에 i를 추가하고
        result.append('+')  # 그리고 result에 +를 추가함
        i += 1  # i에 1을 추가함

    while stk and stk[-1] == arr[idx]:  # 스택이 비어 있지 않고 스택의 top이 현재 arr 원소와 같을 때
        stk.pop()   # 스택에서 pop하고
        result.append('-')  # -를 result에 넣음
        idx += 1
    
    if i > n:
        break

    if idx == n:    # 만약 idx가 n과 같아지면
        break   # 반복문 종료

if not stk:
    for _ in result:
        print(_)
else:
    print('NO')