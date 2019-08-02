def singleNumber(nums):
    """
    问题描述：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均
    出现两次。找出那个只出现了一次的元素。
    说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    解决思路：使用异或运算符，对于^异或运算来说，有以下几个规则
    0 ^ N = N
    N ^ N = 0
    N1^N2^N3 = N1^N3^N2=N2^N3^N1=N2^N1^N3
    所以，N1 ^ N1 ^ N2 ^ N2 ^..............^ Nx ^ Nx ^ N = N
    :param nums:List[int]
    :return:int
    """
    result = 0
    for num in nums:
        result ^= num
    return result
