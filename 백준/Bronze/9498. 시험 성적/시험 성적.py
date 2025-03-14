point = int(input())
test_grade = ''

if 90 <= point <= 100:
        test_grade = 'A'
elif 80 <= point <= 89:
            test_grade = 'B'
elif 70 <= point <= 79:
            test_grade = 'C'
elif 60 <= point <= 69:
            test_grade = 'D'
else:
            test_grade = 'F'

print(test_grade)