# Assessment 3.3: Binary Tree Algorithm and Program for "CAYUNDA"

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


def inorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result


def postorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.val)
    return result


def main():
    print("========================================")
    print("      BINARY TREE TRAVERSALS            ")
    print("========================================")

    # Tree Structure for CAYUNDA
    #        C
    #       / \
    #      A   Y
    #         /
    #        N
    #       / \
    #      U   D
    root = TreeNode('C')
    root.left = TreeNode('A')
    root.right = TreeNode('Y')
    root.right.left = TreeNode('U')
    root.right.left.left = TreeNode('N')
    root.right.left.right = TreeNode('D')

    print(f"Pre-order Traversal:  {' -> '.join(preorder_traversal(root))}")
    print(f"In-order Traversal:   {' -> '.join(inorder_traversal(root))}")
    print(f"Post-order Traversal: {' -> '.join(postorder_traversal(root))}")


if __name__ == "__main__":
    main()