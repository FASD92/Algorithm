"""

첫번째 줄은 int로 n 받고
두번째 줄은 문자열을 sort였나 sorted인가 써서 리스트... 대충 int로 맵핑하고
for문을 len(numbers)만큼 돌면서 더한다

"""
import sys

n = int(sys.stdin.readline())
#print(n)

n2 = sys.stdin.readline().strip()
numbers_str = sorted(n2)
numbers = list(map(int, numbers_str))
#print(numbers)
result = 0

for i in range(len(numbers)):
    result += numbers[i]

print(result)