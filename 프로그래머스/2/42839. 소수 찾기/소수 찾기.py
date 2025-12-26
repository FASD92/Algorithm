"""
문자열의 모든 문자를 순회하며 리스트로 만들어야 한다.
그리고 해당 리스트로 만들 수 있는 모든 경우의 수를 리스트로 만든다.
해당 리스트의 원소를 int형으로 변환 후 소수인지를 체크 후 소수라면 카운트해서 리턴한다.
"""

from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(numbers)
    all_combinations = set()
    
    for i in range(1, len(nums) + 1):
        for p in permutations(nums, i):
            num = int("".join(p))
            all_combinations.add(num)
    
    for num in all_combinations:
        if is_prime(num):
            answer += 1
    
    return answer