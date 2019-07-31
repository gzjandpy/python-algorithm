def selection_sort(arr):
    """
    算法思想： 第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，
    然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。以此类推，
    直到全部待排序的数据元素的个数为零
    时间复杂度： O(n²)
    空间复杂度： O(1)
    稳定性： 不稳定
    :param arr: List[int]
    :return: arr
    """
    n = len(arr)
    for i in range(0, n):
        minimum = i
        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(selection_sort(test_arr))
