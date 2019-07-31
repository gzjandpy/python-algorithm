def max_heap_sort(arr):
    """
    算法思想： 利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，
    并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
    时间复杂度： O(nlogn)
    空间复杂度： O(1)
    稳定性： 不稳定
    :param arr: List[int]
    :return: arr
    """
    n = len(arr)
    for i in range(n - 1, 0, -1):
        max_heapify(arr, i)
    return arr


def max_heapify(arr, end):
    last_parent = (end - 1) // 2
    for parent in range(last_parent, -1, -1):   # 从当前父节点遍历到根节点
        current_parent = parent
        while current_parent <= last_parent:
            child = current_parent * 2 + 1
            if child + 1 <= end and arr[child] < arr[child + 1]:    # 找到较大的孩子节点
                child = child + 1

            if arr[current_parent] < arr[child]:
                arr[current_parent], arr[child] = arr[child], arr[current_parent]
                current_parent = child
            else:
                break
    arr[0], arr[end] = arr[end], arr[0]


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(max_heap_sort(test_arr))
