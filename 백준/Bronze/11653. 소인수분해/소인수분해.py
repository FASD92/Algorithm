"""
11653 소인수 분해

일단 입력 n을 받음
그리고 n을 나눌 숫자인 변수 x를 선언함
x는 당연히 2부터 시작해야 하니 2로 초기화함

일단 n을 x = 2부터 나눈 나머지가 0이 아니면? 즉 소수점이 존재하면 x는 n의 소인수가 아니므로
x += 1을 하고 다시 반복문을 시작한다


"""
import sys

n = int(sys.stdin.readline())
#print(n)

x = 2

while n > 1:
    if n % x == 0:
        print(x)
        n //= x
    else:
        x += 1