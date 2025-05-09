"""
(A**B) % C = ((A**B/2) * (A**B/2)) % C

베이스 케이스는 B, 즉 A의 지수가 0일 때 1을 반납
즉 A^0이 될 때까지 2로 나눔

근데 홀수일 때는 짝수 결과에 a를 곱해줘야함!
"""
import sys
A, B, C = map(int, sys.stdin.read().strip().split())

def recursive(a, b, c):
    if b == 0:  # A의 지수인 B가 0이 될 때까지
        return 1
    divided = recursive(a, b // 2, c)   # 2로 나누는 재귀를 들어간다
    result = (divided * divided) % c
    if b % 2 == 1:  # 만약 b가 홀수면
        result = (result * a) % c   # 짝수의 결과값에 a를 곱해준다!
    return result

print(recursive(A,B,C))