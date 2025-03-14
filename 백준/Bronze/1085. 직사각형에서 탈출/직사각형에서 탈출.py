"""
입력을 x,y,w,h에 int로 변환하고, 이후 리스트로 저장한다.
이후 4개의 비교를 거친다. 모든 비교는 절대값으로 반환한다.
[0-x]
[0-y]
[w-x]
[h-y]
리스트에서 가장 작은 값의 인덱스를 찾아 변수에 저장하고,
해당 위치에 해당하는 변수를 출력한다.

"""
import sys
x,y,w,h = map(int, input().split())

x = abs(0-x)
y = abs(0-y)
w = abs(w-x)
h = abs(h-y)
xywh = [x,y,w,h]

shortcut = xywh.index(min(xywh))

print(xywh[shortcut])