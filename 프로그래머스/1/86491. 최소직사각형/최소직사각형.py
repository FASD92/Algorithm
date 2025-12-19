"""
모든 명함을 담을 수 있는 지갑 중 가장 작은 지갑

경우의 수
- 한 명함의 w,h가 다른 명함보다 크거나 같을 경우에는 해당 명함의 크기로 지갑 크기가 결정됨
- 그렇지 않은 경우, 가로가 가장 긴 명함을 제외한 명함 중 세로가 가장 긴 명함을 뒤집음.
- 재정렬된 명함들의 크기 중 가장 세로가 긴 명함이 최종 지갑 크기의 세로 크기가 됨.


기본 코드는 이건데, 이렇게 하면 for 루프 안에서 max()를 다시 호출하여 계산 복잡도가 O(N^2)가 됨...
게다가 통과도 못했음

"""

def solution(sizes):
    width = []
    height = []
    
    for w, h in sizes:
        if w < h:
            w, h = h, w
        width.append(w)
        height.append(h)
        
    return max(width) * max(height)