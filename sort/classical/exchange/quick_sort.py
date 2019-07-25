def quick_sort(arr):
    """
    算法思想： 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
    时间复杂度： O(nlogn)
    空间复杂度： O(logn)
    稳定性： 不稳定
    :param arr: List[int]
    :return: arr
    """
    n = len(arr)
    arr = quick_sort_recur(arr, 0, n - 1)
    return arr


def quick_sort_recur(arr, first, last):
    if first < last:
        wall = partition(arr, first, last)
        quick_sort_recur(arr, first, wall - 1)
        quick_sort_recur(arr, wall + 1, last)
    return arr


def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:    # 以最后一个元素为基准
            arr[wall], arr[pos] = arr[pos], arr[wall]
            wall += 1

    arr[wall], arr[last] = arr[last], arr[wall]
    return wall


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(quick_sort(test_arr))
