"""
원래 주어진 값을 저장할 original -> int
사이클 변수 count -> int

if N<10:
    N앞에 0을 붙여 두자리 수로 만들어서 다시 저장한다 -> str
else:
    N의 각 자리의 숫자를 int형으로 변환하여 숫자를 더하고 저장 sum -> int
    N의 가장 오른쪽 자리 수와 str로 변환한 sum(len(N)-1)을 이어 붙인다 new -> str
"""

N = input().strip()
original = N

if int(N)<10:
    original = '0'+ N

def cycle(N, count=0):
    total = int(N[0])+int(N[1])
    new_total = str(total)
    new = N[-1]+new_total[-1]
    count += 1

    if new == original:
        return count
    return cycle(new, count)     
   
result = cycle(original)
print(result)