"""
첫째줄 동전 종류 N, 목표 가치 K
(각각의 동전을 매우 많이 갖고 있다)

둘째줄부터 N개의 줄에 동전의 가치 A_i가 오름차순으로 주어짐

A_1 = 1
i>=2 인 경우 A_i는 A_i-1의 배수
-> 그리디 알고리즘을 적용할 수 있는 전제 조건
-> 가장 큰 동전부터 사용하면 항상 최적의 해를 얻을 수 있다

목표
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 함
이 때 필요한 동전 개수의 '최솟값' -> 그리디 알고리즘


필요한 동전 개수를 카운트 할 count = 0 선언
일단 coins라는 리스트를 만들되 내림차순으로 정렬해야함
반복문은 coins의 요소를 모두 하나씩 순회함
coins 원소들을 하나씩 가져오는데
만약 coins[i]가 K보다 크면 넘어감
그리고 coins[i]가 K보다 작거나 같으면 나누고 몫을 count에 += 함
그리고 K를 coin으로 나눈 나머지를 K에 업데이트함
"""
import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)

count = 0

for coin in coins:
    if K == 0:
        break
    if K >= coin:
        count += K // coin
        K %= coin

print(count)