def shell_sort(arr):
    """
    算法思想： 把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
    时间复杂度： O(n²)
    空间复杂度： O(1)
    稳定性： 不稳定
    :param arr: List[int]
    :return: arr
    """
    n = len(arr)
    gap = n // 2    # 分隔距离，也是组数
    while gap > 0:
        index = gap
        while index < n:
            element = arr[index]
            pos = index
            while pos-gap >= 0 and arr[pos-gap] > element:
                arr[pos] = arr[pos-gap]
                pos -= gap
            arr[pos] = element
            index += 1
            print(arr)
        gap = gap // 2
    return arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(test_arr)
    shell_sort(test_arr)
