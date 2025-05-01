"""
신입사원을 최대로 뽑을 수 있는?

서류 순위, 면접 순위 튜플
동차석은 없음

1. 정렬 기준 -> 서류 순위(오름차순)
2. 선택 기준 -> 이전에 뽑은 사람 중 가장 좋은 면접 등수보다 더 좋아야(숫자가 더 작아야) 선택
3. 갱신 기준 -> count 증가, min_interview(최소 면접 등수)를 현재 면접 등수로 갱신
그래야 다음 사람은 min_interview보다 등수가 좋아야(숫자가 더 낮아야)선택될 수 있으니까

"""
import sys
T = int(sys.stdin.readline())

for i in range(T):
#print(T)
    N = int(sys.stdin.readline())
    grade = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    grade.sort(key=lambda x: (x[0], x[1]))
    #print(grade)
    min_interivew = grade[0][1]
    count = 1

    for i in range(1, N):
        if grade[i][1] < min_interivew:
            count += 1
            min_interivew = grade[i][1]
    print(count)
