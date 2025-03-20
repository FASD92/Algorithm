"""
교재였나 어디선가 봤던 것이라...
핵심 개념은 반복문으로 목록에서 하나씩 가져오는 것
그리고 스택을 하나 만들어서 이전 상황을 저장하는 것

입력은 한줄씩 개행문자 제거해서 문자열로 받고 string
빈 스택 stk 선언
반복문은 문자열(의 길이만큼)
만약 i = '('
    stk.append('i')
    elif i = ')'
        if not stk # 스택이 비어있지 않다면
            return 'NO' # VPS가 안 되니까 NO를 반환
        stk.pop() # 스택에 뭐가 있는데 )를 입력 받으면 스택을 비움
    위 절차들이 끝나고 stk에 뭐가 없으면 False지만 not을 붙이고 YES를 출력
    그게 아니면 NO를 출력

이제 주어진 T만큼 반복문으로 이 함수를 돌릴 건데
함수의 인자로 들어갈 s를 readline().strip()으로 한줄씩 저장함
"""
import sys

T = int(sys.stdin.readline().strip())

def parentheses(s):
    stk = []
    for i in range(len(s)):
        line = s
        if line[i] == '(':
            stk.append('(')
        elif line[i] == ')':
            if not stk:
                return 'NO'
            stk.pop()
    if not stk:
        return 'YES'
    else:
        return 'NO'
    
for j in range(T):
    s = sys.stdin.readline().strip()
    result = parentheses(s)
    print(result)