# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def reverseList1(head):
    """
    问题描述：反转一个单链表。你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
    解决思路：本题用递归。用curr保存当前head的位置，pre保存上一个head的位置
    :param head:ListNode
    :return:ListNode
    """
    pre = None
    while head:
        curr = head
        head = head.next
        curr.next = pre
        pre = curr
    return pre


def reverseList2(head):
    """
    问题描述：反转一个单链表。你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
    解决思路：本题用递归。new_head在递归过程不变，始终指向最后一个节点，head则从倒数
    第二个节点依次向前退
    :param head:ListNode
    :return:ListNode
    """
    if not head or not head.next:
        return head
    new_head = reverseList2(head.next)
    next_node = head.next
    next_node.next = head
    head.next = None
    return new_head

