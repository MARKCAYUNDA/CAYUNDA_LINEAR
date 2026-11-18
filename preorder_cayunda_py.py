# Assessment 3.6: Preorder Traversal (Root -> Left -> Right)
# Student: MARK CAYUNDA

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def preorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)
    return result

def main():
    print("==================================================")
    print("   ASSESSMENT 3.6: PREORDER TRAVERSAL (DFS)       ")
    print("   Name: MARK CAYUNDA                             ")
    print("==================================================\n")

    # Binary Tree Structure (Level-order insertion of MARK CAYUNDA):
    #             M
    #           /   \
    #          A     R
    #         / \   / \
    #        K   C A   Y
    #       / \ / \
    #      U  N D  A

    root = TreeNode('M')
    root.left = TreeNode('A')
    root.right = TreeNode('R')

    root.left.left = TreeNode('K')
    root.left.right = TreeNode('C')
    root.right.left = TreeNode('A')
    root.right.right = TreeNode('Y')

    root.left.left.left = TreeNode('U')
    root.left.left.right = TreeNode('N')
    root.left.right.left = TreeNode('D')
    root.left.right.right = TreeNode('A')

    print("Preorder Traversal (Root -> Left -> Right):")
    print(" -> ".join(preorder_traversal(root)))

if __name__ == "__main__":
    main()