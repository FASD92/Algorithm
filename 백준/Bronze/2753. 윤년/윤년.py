"""
입력 연도값을 정수로 받고 입력 연도값이 4의 배수인지 확인한다.
만약 입력을 4로 나눴을 때 나머지가 0이면 4의 배수다.
4년의 배수일  경우에는 1이지만,
만약 100년의 배수이면서 400년의 배수가 아니면 0이고,
400년의 배수일 경우에는 1이다.
그 외에는 0이다.


"""

yoon = ''

year = int(input())
if year%4 == 0:
    yoon = '1'
    if year%100 == 0 and year%400 !=0:
        yoon = '0'
    elif year%400 == 0:
        yoon ='1'
else:
    yoon = '0'

print(yoon)