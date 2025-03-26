"""
모듈러 연산

(10**11) % 12
(10%12) ** (11%12) % 12

base case는 지수가 0일 때 1을 return
재귀로 지수가 0이 될 때까지 내려가는 거임
result는 짝수 기준인데,
half*half를 하는 이유는
n**x = n**(x/2) * n**(x/2) 이기 때문
"""
import sys
A, B, C = map(int, sys.stdin.read().strip().split())

def mod_pow(a, b, c):
    if b == 0:
        return 1
    half = mod_pow(a, b // 2, c)
    result = (half * half) % c
    if b % 2 == 1:
        result = (result * a) % c
    return result

print(mod_pow(A,B,C))