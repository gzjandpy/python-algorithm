def insertion_sort(arr):
    """
    算法思想： 每次将一个待排序的记录，按其关键字大小插入到前面已经排好序的子序列中的适当位置，直到全部记录插入完成为止。
    时间复杂度： O(n²)
    空间复杂度： O(1)
    稳定性： 稳定
    :param arr: List[int]
    :return: arr
    """
    n = len(arr)
    for i in range(1, n):
        element = arr[i]
        pos = i

        while pos >= 1 and arr[pos - 1] > element:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = element
    return arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(insertion_sort(test_arr))
