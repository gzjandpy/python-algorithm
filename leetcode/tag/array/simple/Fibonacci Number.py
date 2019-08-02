def fib(N):
    """
    问题描述：斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。
    该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
    给定 N，计算 F(N)。
    解决思路： 可使用递归， 但运行时间长。使用下面这种方法可大大减少时间复杂度
    :param N:
    :return:
    """
    a, b = 0, 1
    for _ in range(N):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    test_N = 4
    print(fib(test_N))
