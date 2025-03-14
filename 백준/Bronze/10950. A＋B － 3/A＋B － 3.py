"""
readline을 할 때마다 한 줄씩 불러온다
첫째 줄에 테스트 케이스의 개수 T가 주어지므로 이를 T에 저장한다.
T+1만큼 반복하여 readline을 불러온다.
불러온 문자열을 공백으로 split하여 리스트로 저장 후, 이를 int로 맵핑한 리스트의 모두 더한 값을 프린트한다.
"""
import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    numbers = sys.stdin.readline().split()
    int_numbers = list(map(int, numbers))
    print(sum(int_numbers))