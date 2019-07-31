def counting_sort(arr):
    """
    算法思想: 其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，
    计数排序要求输入的数据必须是有确定范围的整数。
    时间复杂度： O(n+k),k为最大数
    空间复杂度： O(n+k)
    :param arr: List[int]
    :return: arr
    """
    k = max(arr)
    n = len(arr)
    temp_arr = [0] * (k+1)
    for i in range(n):
        temp_arr[arr[i]] += 1

    for i in range(1, k+1):
        temp_arr[i] = temp_arr[i-1] + temp_arr[i]

    result_arr = arr.copy()
    for i in range(n-1, -1, -1):
        result_arr[temp_arr[arr[i]] - 1] = arr[i]
        temp_arr[arr[i]] -= 1

    return result_arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(counting_sort(test_arr))
