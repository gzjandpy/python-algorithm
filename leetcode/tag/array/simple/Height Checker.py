def heightChecker(heights):
    """
    问题描述：学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
    请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以非递减高度排列的必要移动人数。
    解决思路：创建一个排序后的新数组， 统计不一样的元素的个数
    :param heights:List[int]
    :return:int
    """
    B = sorted(heights)
    i, j, nums = 0, 0, 0
    while j < len(B):
        if heights[i] != B[j]:
            nums += 1
        i += 1
        j += 1
    return nums
    """
    一行解决： return sum(i != j for i, j in zip(heights, sorted(heights)))
    """


if __name__ == "__main__":
    test_arr = [1, 1, 4, 2, 1, 3]
    print(heightChecker(test_arr))
