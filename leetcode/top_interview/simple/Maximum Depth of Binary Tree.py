# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def maxDepth1(root):
    """
    问题描述：给定一个二叉树，找出其最大深度。二叉树的深度为根节点到
    最远叶子节点的最长路径上的节点数。
    解决思路：借助栈实现DFS
    说明: 叶子节点是指没有子节点的节点。
    :param root:TreeNode
    :return:int
    """
    if not root:
        return 0

    max_depth = 0
    node_stack = [root]
    value_stack = [1]
    while node_stack:
        node = node_stack.pop()
        value = value_stack.pop()
        max_depth = max(max_depth, value)
        if node.right:
            node_stack.append(node.right)
            value_stack.append(value + 1)
        if node.left:
            node_stack.append(node.left)
            value_stack.append(value + 1)
    return max_depth


def maxDepth2(root):
    """
    借助队列实现BFS
    :param root: TreeNode
    :return: int
    """
    if not root:
        return 0
    depth = 0
    from collections import deque
    queue = deque([root])
    while not queue:
        depth += 1
        n = len(queue)
        while n > 0:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            n -= 1
    return depth
