def isToeplitzMatrix(matrix):
    """
    问题描述：如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
    给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。
    解决思路：从第二行起，每行的最后n-1个元素应该和上一行的前n-1个元素相同
    :param matrix:List[List[int]]
    :return:Bool
    """
    for i, r in enumerate(matrix):
        if i == 0:
            continue
        if r[1:] != matrix[i - 1][0:-1]:
            return False
    return True
"""
一般方法：
def isToeplitzMatrix(matrix):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r-1):
            for j in range(0, c-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
"""

if __name__ == "__main__":
    test_arr = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(isToeplitzMatrix(test_arr))
