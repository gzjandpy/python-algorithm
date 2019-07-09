def bubble_sort(arr):
    """
    算法思想： 依次比较两个相邻的元素，如果他们的顺序（如从大到小）错误就把他们交换过来, 重复n-1次即可完成排序
    时间复杂度： O(n²)
    空间复杂度： O(1)
    稳定性： 稳定
    :param arr: List[int]
    :return: arr
    """
    n = len(arr)
    for x in range(1, n):       # 需要n-1趟
        for i in range(0, n-x):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(bubble_sort(test_arr))
