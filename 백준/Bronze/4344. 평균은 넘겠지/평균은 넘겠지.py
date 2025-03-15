"""
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다
학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다.
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여
소수점 셋째 자리까지 출력한다.
정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.


readline()을 이용해 테스트케이스 변수를 int형으로 저장한다.
이후 반복문을 이용해 readline()으로 한 줄씩 읽어와 리스트로 저장한다.
이 때 공백이 있으니 split으로 공백을 제거하여 저장할 수 있도록 한다.
arr[0]은 학생의 수이므로 int형으로 저장하고,
인덱스 슬라이싱으로 얕은 복사를 하고 int형으로 맵핑해서 학생들의 점수가 담긴 리스트로 선언한다.

이중 반복문을 이용하는데 새롭게 만들어진 arr의 len만큼 반복한다.
학생들의 점수가 담긴 리스트의 총합을 학생수로 나눠서 평균을 저장한다.
만약 현재 선택된 점수가 평균보다 높을 시 temp +=1 을 한다.
이후 round와 f스트링 :.nf를 이용해 출력한다
"""
import sys

T = int(sys.stdin.readline())
total = 0
temp = 0

for i in range(T):
    arr = list(sys.stdin.readline().split())
    count = int(arr[0])
    points = list(map(int,arr[1:]))
    avg = sum(points) / count
    temp = 0
    for s in range(len(points)):
        if points[s] > avg:
            temp += 1
    print(f'{round(((temp/count)*100),3):.3f}''%')