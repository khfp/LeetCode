# Definition for a binary tree node.
class TreeNdoe:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树类
class Tree:
    # 初始化
    def __init__(self):
        self.root = TreeNdoe()

    # 二叉树的实现
    # 待补充

    # 前序遍历（递归）
    def pre_oder_recursion(self, root):
        if not root:
            return None
        print(root.val)
        self.pre_oder_recursion(root.left)
        self.pre_oder_recursion(root.right)

    # 前序遍历（堆栈）
    def pre_oder_srack(self, root):
        if not root:
            return None
        node, stack = root, []
        while stack or node:
            while node:
                print(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    # 中序遍历（递归)
    def in_order_recursion(self, root):
        if not root:
            return None
        self.in_order_recursion(root.left)
        print(root.val)
        self.in_order_recursion(root.right)

    # 中序遍历(堆栈)
    def in_order_stack(self, root):
        if not root:
            return None
        node, stack = root, []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val)
            node = node.right

    # 后序遍历(递归)
    def post_oder_recursion(self, root):
        if not root:
            return None
        self.post_oder_recursion(root.left)
        self.post_oder_recursion(root.right)
        print(root.val)

    # 后序遍历（堆栈）
    def post_order_stack(self, root):
        if not root:
            return None
        node, stack1, stack2 = root, [], []
        while node or stack1:
            while node:
                stack2.append(node)
                stack1.append(node)
                node = node.right
            node = stack1.pop()
            node = node.left
        while stack2:
            print(stack2.pop().val)

    # 层序遍历
    def level_order_stack(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop(0)
            print(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
