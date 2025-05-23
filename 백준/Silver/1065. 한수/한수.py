"""
if N이 99보다 작거나 같으면, 즉 자릿수가 1~2이면 print N
else, 즉 자릿수가 세자리수 이상이면
이중 반복문으로 N의 각 자리수가 등차수열을 이루는지 확인

근데 등차수열인 걸 어떻게 확인하지?
음 등차가 음수일 수도 있겠네
예를 들어 864는 등차가 -2인 등차수열..

그럼 예를 들어서
a = i[1] - i[2]이라 해보자(형변환은 해줘야겠지만)
그리고
b = i[2] - i[3]라 해보자
a == b 라면, 등차수열이므로 count += 1을 하고 아니라면, 즉 a != b라면 continue를 하면 될 것 같다.
"""

N = input()
length = len(N)
count = 0

if length <= 2:
    print(N)
else:
    for i in range(100, int(N) + 1):
        a = int(str(i)[0]) - int(str(i)[1])
        b = int(str(i)[1]) - int(str(i)[2])
        if a == b:
            count += 1
        else:
            continue
    print(count + 99)