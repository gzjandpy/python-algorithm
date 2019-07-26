def sortedSquares(A):
    """
    问题描述：给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，
            要求也按非递减顺序排序。
    解决思路： 设立头尾两个指针， 比较其绝对值大小， 大的那个即在数组B的后面
    :param A:
    :return:
    """
    n = len(A)
    B = [None for _ in A]
    index, left, right = n - 1, 0, n - 1
    while index >= 0:
        if abs(A[left]) < abs(A[right]):
            B[index] = A[right] ** 2
            right -= 1
        else:
            B[index] = A[left] ** 2
            left += 1
        index -= 1
    return B


if __name__ == "__main__":
    test_arr = [-7, -6, -2, 0, 8, 9]
    print(sortedSquares(test_arr))
