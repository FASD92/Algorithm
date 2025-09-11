import sys
input = sys.stdin.readline

count_dict = {}

word = input().strip()
upper_word = word.upper()       # 대소문자를 구분하지 않으므로 .upper 또는 .lower로 통일함

for char in upper_word:         # 해당 단어에 문자를 하나씩 체크하여 count_dict에 추가
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

max_count = max(count_dict.values())    # count_dict의 values만 추려서 max 값을 취함
max_chars = []
for key, value in count_dict.items():   # .items는 키와 밸류를 모두 취할 수 있는데, 값이 max_count인지 비교하고, 조건을 만족하면 그 키를 모아야 하므로 .items가 적합함
    if value == max_count:
        max_chars.append(key)

if len(max_chars) > 1:
    print("?")
else:
    print(max_chars[0])