"""
빈 스택을 선언 stk -> stack
readline()으로 입력 받은 첫째 줄을 .strip()으로 개행 문자 제거 후
테스트 케이스 T로 선언 -> int

반복문을 range(T)
readline()을 실행해서 function으로 선언 -> str
5개의 멍청한 하드코딩을 하는데 push X가 문제임
만약 function[1]='u'이면
function을 공백을 기준으로 나누고 2번째 항목을 X로 저장해야함 -> int
그리고 push(X)를 하는 거임
그 외에는 간단함
if function[p]='p'
    print(stk.pop())
elif function[0]='s'
    print(len(stk))
elif function[0]='e'
    if stk.is_empty:
        print('1')
    else:
        print('0')
elif function[0]='t'
    if stk.is_empty:
        print('-1')
    else:
        print(stk.peek())

"""

import sys

stk = []

T = int(sys.stdin.readline().strip())

for i in range(T):
    function = sys.stdin.readline().strip()

    if function[1] == 'u':
        function = function.split()
        X = int(function[1])
        stk.append(X)

    elif function[0] == 'p':
        if stk:
            print(stk.pop())
        else:
            print(-1)

    elif function[0] == 's':
        print(len(stk))

    elif function[0] == 'e':
        if stk:
            print(0)
        else:
            print(1)

    elif function[0] == 't':
        if stk:
            print(stk[-1])
        else:
            print(-1)