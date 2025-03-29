"""
노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.
이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

일단 이걸 원복해서 다시 트리 형식으로 바꿔야 할 거 같은데...
전위 순회는 root, left, right 순
이진 검색 트리는 왼쪽 서브트리는 루트보다 작고, 오른쪽 서브트리는 루트보다 큰 구조임
원복만 하면 트리 순회에서 postorder 함수 복붙해도 될 듯

예제 입력을 한 줄로 바꾸면
50 30 24 5 28 45 98 52 60

50은 루트
왼쪽 서브트리는 30부터 28까지
오른쪽 서브트리는 45부터 끝까지

50보다 큰 놈을 찾을 때까지 반복문하고
left랑 right로 나누면 될 것 같은데
idx를 쓰고 idx+=1을 써야 하나
아니면 start랑 end만 있으면 되나
"""
import sys
sys.setrecursionlimit(10**6)

preorder = [int(line.strip()) for line in sys.stdin]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build(start, end):
    if start > end:
        return None

    root_val = preorder[start]
    idx = start + 1

    while idx <= end and preorder[idx] < root_val:
        idx += 1

    node = Node(root_val)
    node.left = build(start + 1, idx - 1)
    node.right = build(idx, end)

    return node

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

root = build(0, len(preorder) - 1)
postorder(root)