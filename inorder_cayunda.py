# Assessment 3.6: Inorder Traversal (Left -> Root -> Right)
# Student: MARK CAYUNDA

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def inorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result

def main():
    print("==================================================")
    print("   ASSESSMENT 3.6: INORDER TRAVERSAL (DFS)        ")
    print("   Name: MARK CAYUNDA                             ")
    print("==================================================\n")

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

    print("Inorder Traversal (Left -> Root -> Right):")
    print(" -> ".join(inorder_traversal(root)))

if __name__ == "__main__":
    main()