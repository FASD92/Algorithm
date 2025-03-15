"""
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다.
O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

readline()을 이용해 테스트 케이스의 개수 값을 읽고 int형으로 변수 선언
총 점수를 저장할 변수 선언
연속된 O의 점수를 누적할 temp 변수 선언

반복문을 사용하여 테스트 케이스 횟수만큼 readline()으로 문자열을 리스트로 저장하고
이중 반복문을 이용하여 리스트 arr[i]이 O인지 확인한다
O일 경우 temp 변수에 +=1, 그 외에의 경우에는 temp를 0으로 초기화 한다
이후 총 점수에 현재 temp변수의 값을 추가하여 저장한다.
이중 반복문은 len(리스트-1)만큼 반복한다.
이중 반복문의 프로세스가 모두 끝나면 총 점수를 출력하고 총 점수와 temp 변수를 초기화 한다.
"""
import sys
T = sys.stdin.readline()

total = 0
temp = 0

for i in range(int(T)):
	arr = sys.stdin.readline()
	for s in range(len(arr)-1):
		if arr[s] == 'O':
			temp += 1
		else:
			temp = 0
		total += temp
	print(total)
	total = 0
	temp = 0