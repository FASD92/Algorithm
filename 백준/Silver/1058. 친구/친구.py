"""
2-친구는 친구이거나, 친구의 친구

a와 b가 친구면 b와 a도 친구
a와 a는 친구가 아니다

a와 b가 친구이거나, a와 친구이고 b와 친구인 c가 존재하면 a는 b의 2-친구다

3중 for문 사용
일단 2중 for문으로 2차원 리스트를 탐색
만약 i==j면 a와 a는 친구가 아니다를 만족하니 continue
만약 Y인 원소를 만나면 a와 b가 친구이거나를 만족하니 count += 1
그리고 for문을 하나 더 돌아서 a와 친구이며 b와 친구인 c가 존재한다면 count += 1

그리고 most_famous라는 변수를 만들어야함
왜냐면 그냥 count 하나로는 원하는 답을 출력할 수 없음
왜냐면 '가장 유명한' 사람의 2-친구가 필요한 거니까

그리고 반복문 시작할 때 count = 0으로 초기화해서 다음 행으로 넘어갈 때마다 리셋
"""
import sys
n = int(sys.stdin.readline().strip())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

most_famous = 0

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] == 'Y':
            count += 1
        else:
            for k in range(n):
                if graph[i][k] == 'Y' and graph[j][k] == 'Y':
                    count += 1
                    break
    if count > most_famous:
        most_famous = count

print(most_famous)