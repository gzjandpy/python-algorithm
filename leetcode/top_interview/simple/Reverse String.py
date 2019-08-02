def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    问题描述：编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[]
    的形式给出。不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外
    空间解决这一问题。你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符
    解决思路：遍历一半数组，交换
    """
    n = len(s)
    for i in range(0, n // 2):
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
    return s
