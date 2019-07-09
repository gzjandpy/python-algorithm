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
    gap = n // 2
    while gap > 0:
        y_index = gap
        while y_index < n:
            y = arr[y_index]
            x_index = y_index - gap
            while x_index >= 0 and arr[x_index] > y:
                arr[x_index + gap] = arr[x_index]
                x_index -= gap
            arr[x_index + gap] = y
            y_index += 1
        gap = gap // 2
    return arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(shell_sort(test_arr))
