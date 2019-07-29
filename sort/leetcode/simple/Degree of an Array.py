def findShortestSubArray(nums):
    """
    问题描述：给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素
    出现频数的最大值。你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
    解决思路：建立一个记录元素第一次出现位置的字典first，一个元素出现次数的字典counter，判断当前degree和当前元素次数
    的大小关系
    :param nums:
    :return:
    """
    first, counter, degree, res = {}, {}, 0, 0
    for i, v in enumerate(nums):

        if v not in first:
            first[v] = i

        counter[v] = counter.get(v, 0) + 1
        if counter[v] > degree:
            degree = counter[v]
            res = i - first[v] + 1
        elif counter[v] == degree:
            res = min(res, i - first[v] + 1)
    return res


if __name__ == "__main__":
    test_arr = [1, 2, 2, 3, 1, 4, 2]
    print(findShortestSubArray(test_arr))
