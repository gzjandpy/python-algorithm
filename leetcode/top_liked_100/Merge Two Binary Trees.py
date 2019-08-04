# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def mergeTrees(t1, t2):
    """
    问题描述： 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，
    两个二叉树的一些节点便会重叠。你需要将他们合并为一个新的二叉树。合并
    的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的
    节点将直接作为新二叉树的节点。
    解决思路： 利用BFS，对两棵树分别使用两个队列
    :param t1:
    :param t2:
    :return:
    """
    from collections import deque
    if not (t1 and t2):
        return t1 or t2
    queue1, queue2 = deque([t1]), deque([t2])
    while queue1 and queue2:
        node1, node2 = queue1.popleft(), queue2.popleft()
        if node1 and node2:
            node1.val += node2.val
            if (not node1.left) and node2.left:
                node1.left = TreeNode(0)
            if (not node1.right) and node2.right:
                node1.right = TreeNode(0)
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.left)
            queue2.append(node2.right)
    return t1
