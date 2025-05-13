"""
재귀호출 방식에 비해 DP가 얼마나 빠른지 알아보자
아래는 의사코드

fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
"""
import sys
n = int(sys.stdin.readline())
#print(n)
count_r = 0
count_f = 0
fib = []
result = []

def recursion(n):
    global count_r
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        count_r += 1
        return 1
    else:
        return recursion(n - 1) + recursion(n - 2)
    
recursion(n)
result.append(count_r)

def fib(n):
    global count_f
    fib = [0] * (n + 1)
    fib[1], fib[2] = 1, 1
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        count_f += 1
    return fib[n]

fib(n)
result.append(count_f)

print(*result)