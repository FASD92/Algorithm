"""
sys를 import한다.
정답변수를 문자열로 선언한다.
readline()으로 테스트케이스를 int형으로 변환하여 저장.

이후 테스트케이스만큼 반복문
공백을 기준으로 split하고 첫번째 항목은 int형으로 변환해 문자 반복 R로 저장
두번째 항목은 '반복해야 할 문자'로 저장

이중 반복문은 반복해야 할 문자의 길이만큼 반복
삼중 반복문은 R만큼 반복
정답변수에 반복해야 할 문자의 현재 인덱스에 해당하는 문자를 더하고 반복변수에 1을 추가한다
첫 반복문이 끝날 때마다 정답변수를 출력한다.
"""

import sys
k = 0

T = int(sys.stdin.readline())

for i in range(T):
	arr = sys.stdin.readline().split()
	R = int(arr[0])
	string = arr[1]
	answer = ''
	for j in range(len(string)):
		while k < R:
			answer += string[j]
			k+=1
		k = 0
	print(answer)