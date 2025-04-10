"""
2원짜리 동전 무한히
5원짜리 동전 무한히
동전의 개수가 최소 -> 그리디?
근데 동전의 금액이 상위 동전의 배수가 아님...

거스름돈 액수 N
a = 2
b = 5
동전의 '최소' 개수를 출력할 minimum_count
5로 나눴을 때 몫 divided_5
5원으로 나눈 '이후의 값' after_b
after_b에 다시 2를 나눴을 때 몫 divided_2


일단 N을 b로 나눠서 나머지가 0이 되면 그게 best임
하지만 N을 b로 나눠서 떨어지지 않으면 b를 1씩 줄여가면서 해를 찾아야 함

참고로 나눌 수 없는 경우에는 -1을 출력함

반복문은 divided_5가 0보다 클 때는 무한히 반복함
N에서 5(5원이니까) * N을 5로 나눈 몫만큼 빼서 after_b에 저장함
after_b에서 2로 나누어 떨어지면 그게 정답이므로 print(divided_5 + divided 2)를 하고
반복문을 빠져 나옴


"""
N = int(input())
a = 2
b = 5
minimum_count =0

divided_5 = N // 5

while divided_5 >= 0:
    after_b = N - (5 * divided_5)
    if after_b % 2 == 0:
        divided_2 = after_b // 2
        print(divided_5 + divided_2)
        break
    divided_5 -= 1
else:
    print(-1)