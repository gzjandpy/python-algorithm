def transpose(A):
    """
    问题描述：给定一个矩阵 A， 返回 A 的转置矩阵。
    矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
    解决思路：将行数和列数互换
    :param A:
    :return:
    """
    R = len(A)
    C = len(A[0])
    answer = []
    for c in range(C):
        nums = []
        for r in range(R):
            nums.append(A[r][c])
        answer.append(nums)
    return answer

    """
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    """


if __name__ == "__main__":
    test_arr = [[1,2,3],[4,5,6]]
    print(transpose(test_arr))
