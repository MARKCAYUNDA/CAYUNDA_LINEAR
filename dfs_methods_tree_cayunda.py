# Assessment 3.6: DFS Methods in Tree (Preorder, Inorder, Postorder)
# Student: MARK CAYUNDA

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# 1. Preorder Traversal: Root -> Left -> Right
def preorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.val)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)
    return result

# 2. Inorder Traversal: Left -> Root -> Right
def inorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result

# 3. Postorder Traversal: Left -> Right -> Root
def postorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.val)
    return result

def main():
    print("==================================================")
    print("   ASSESSMENT 3.6: DFS METHODS IN BINARY TREE     ")
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

    print("Preorder  (Root -> Left -> Right):")
    print(" -> ".join(preorder_traversal(root)))

    print("\nInorder   (Left -> Root -> Right):")
    print(" -> ".join(inorder_traversal(root)))

    print("\nPostorder (Left -> Right -> Root):")
    print(" -> ".join(postorder_traversal(root)))

if __name__ == "__main__":
    main()