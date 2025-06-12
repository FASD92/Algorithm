"""
int형 10진수 변수 = int(n진수 문자열, n)

만약 문자열의 첫번째 문자가 0이면
    그 문자열의 두번째 문자가 x면 16진수로 출력
    그 문자열의 두번째 문자가 x가 아니면 8진수로 출력
그게 아니면, 즉 문자열의 첫번째 문자가 0이 아니면
그대로 int 변환해서 출력
"""
import sys

n = sys.stdin.readline()
#print(n[0])
result = '0'

if n[0] == '0':
    if n[1] == 'x':
        result = int(n, 16)
    else:
        result = int(n, 8)
else:
    result = int(n)

print(result)