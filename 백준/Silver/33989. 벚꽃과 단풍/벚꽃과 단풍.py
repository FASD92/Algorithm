import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0].strip())
    s = data[1].strip()
    
    total_B = s.count('B')
    left_D = 0
    min_cost = total_B  # k=0일 때 비용 (모든 동전을 D로 만들기 위한 비용)
    
    for k in range(1, n + 1):
        if s[k - 1] == 'D':
            left_D += 1
        cost = 2 * left_D + total_B - k
        if cost < min_cost:
            min_cost = cost
            
    print(min_cost)

if __name__ == "__main__":
    main()