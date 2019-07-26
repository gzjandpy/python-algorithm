def sortArrayByParityII(arr):
    """
    问题描述： arr中的元素其中一半是奇数，另一半是偶数，要求把奇数放在奇数位置上， 偶数放在偶数位置上
    解决思路： 若奇数位置上是奇数，则跳到下一奇数位置上，否则将奇数位置和偶数位置上的数交换，如此反复直到奇数位置跳出数组
    时间复杂度： O(n)
    空间复杂度： O(1)
    :param arr: List[int]
    :return: arr
    """
    even_pos, odd_pos, n = 0, 1, len(arr)
    while odd_pos < n:
        if arr[odd_pos] % 2 != 0:
            odd_pos += 2
        else:
            arr[even_pos], arr[odd_pos] = arr[odd_pos], arr[even_pos]
            even_pos += 2
    return arr


if __name__ == "__main__":
    test_arr = [9, 6, 2, 9, 3, 8]
    print(sortArrayByParityII(test_arr))
