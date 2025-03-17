"""
재귀함수를 이용한다
만약 i가 1이면 1을 리턴하고
아니면 n*fac(i-1)을 하고 리턴
"""
import sys
n = int(sys.stdin.read())

def fac(n):
    if n<=0:
        return 1
    return n*fac(n-1)

print(fac(n))