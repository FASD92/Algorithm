"""
readlines()로 여러 줄의 입력을 리스트로 읽어 온다.
리스트의 항목들을 하나씩 불러와 '/n'을 ''으로 replace하여 저장한다.
리스트의 맨 마지막 항목에는 개행문자가 없으니 len(arr)-1만큼 반복한다.
다시 리스트를 int로 맵핑하여 저장한다.
max함수로 리스트의 최댓값을 저장하고, 저장한 걸 다시 index 함수로 index를 저장한다.
print는 출력이 두 줄로 이뤄졌으니 개행문자를 사용해 출력해보자
"""
import sys
arr = sys.stdin.readlines()

for i in range(len(arr)-2):
	arr[i] = arr[i].replace('\n','')

int_arr = list(map(int,arr))
max_val = max(int_arr)
index_val = int_arr.index(max_val)

print(f'{max_val}\n{index_val+1}')