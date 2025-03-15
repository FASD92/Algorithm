"""
sys.stdin.read()를 이용해 리스트를 만든다.
해당 리스트는 'N A'로 저장될테니 이를 공백을 기준으로 split하고 int로 맵핑하여 각각 변수로 저장한다.
한번더 sys.stdin.read()를 이용해 리스트를 만든다.
해당 리스트도 위와 동일하게 항목들을 int로 변환한다.

A와 seq[i]의 값을 비교 후 만약 seq[i]의 값이 A보다 같거나 크면
pop(i) 함수로 항목을 삭제 후 반환한다.
pop(i) 함수 사용시 순차적으로 반복하면 pop에 의해 index가 건너뛸 수도 있으니
range는 len(seq)-1,-1,-1로 설정하여 리스트의 뒤에서부터 실행한다.

출력을 1 4 2 3처럼 한 줄로 보여줘야 하니 이를 위한 반복문도 작성한다.

"""
import sys

inf = sys.stdin.readline().split()
N, A = map(int, inf)
i = 0
s = 0
arr = ''

inf2 = sys.stdin.readline().split()
seq = list(map(int,inf2))

for i in range(len(seq)-1,-1,-1):
    if A <= seq[i]:
        seq.pop(i)

for s in range(len(seq)):
    arr += str(seq[s])+' '
    
print(arr)
