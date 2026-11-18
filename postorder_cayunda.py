# Assessment 3.6: Postorder Traversal (Left -> Right -> Root)
# Student: MARK CAYUNDA

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

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
    print("   ASSESSMENT 3.6: POSTORDER TRAVERSAL (DFS)      ")
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

    print("Postorder Traversal (Left -> Right -> Root):")
    print(" -> ".join(postorder_traversal(root)))

if __name__ == "__main__":
    main()