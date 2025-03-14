import sys
data = sys.stdin.readlines()
data[0] = data[0].replace('\n','')
a,b = map(int,data)

print(a+b)