import sys

def preorder(node):
    if node != '.':
        print(node, end='')  # 루트
        preorder(tree_dict[node][0])  # 왼쪽
        preorder(tree_dict[node][1])  # 오른쪽


# 2. 중위 순회
def inorder(node):
    if node != '.':
        inorder(tree_dict[node][0])  # 왼쪽
        print(node, end='')  # 루트
        inorder(tree_dict[node][1])  # 오른쪽


def postorder(node):
    if node != '.':
        postorder(tree_dict[node][0])
        postorder(tree_dict[node][1])
        print(node, end='')


n = int(sys.stdin.readline().strip())
tree_dict = {}
for _ in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree_dict[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')