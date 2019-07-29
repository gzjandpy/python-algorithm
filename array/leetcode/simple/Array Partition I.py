def arrayPairSum(nums):
    """
    问题描述： 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对,
    例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
    解决思路： 将数组排序， 偶数项的和即为所求
    :param nums:List[int]
    :return:
    """
    nums.sort()
    return sum(nums[::2])


if __name__ == "__main__":
    test_arr = [8, 9, 4, 3, 10, 2]
    print(arrayPairSum(test_arr))
