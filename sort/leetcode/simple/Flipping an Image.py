def flipAndInvertImage(A):
    """
    问题描述： 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
            水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
            反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
    解决思路： 直接编写两个函数，一个用来将数组倒序， 一个用来将1，0互换
    :param A: List[List[int]]
    :return:   A
    """
    def flip(A):
        for row in A:
            row_length = len(row)
            for i in range(row_length // 2):
                row[i], row[row_length - 1 - i] = row[row_length - 1 - i], row[i]

    def invert(A):
        for row in A:
            row_length = len(row)
            for i in range(row_length):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1

    flip(A)
    invert(A)
    return A


if __name__ == "__main__":
    test_A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    print(flipAndInvertImage(test_A))
