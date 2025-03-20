"""
첫 번째 줄 정수 K 입력을 readline().strip()으로 입력 받고 int형으로 저장
빈 스택 stk 선언
반복문 range는 K
K가 0일 경우에는 pop()으로 제거하고
아니면 append(K)
된다면 print(sum(stk))

"""
import sys

K = int(sys.stdin.readline().strip())
stk = []

for i in range(K):
    num = int(sys.stdin.readline().strip())
    
    if num == 0:
        if stk:
            stk.pop()
    else:
        stk.append(num)

print(sum(stk))