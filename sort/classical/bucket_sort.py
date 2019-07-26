def bucket_sort(arr):
    """
    算法思想： 假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序
    时间复杂度： O(n+k)
    空间复杂度： O(n+k)
    稳定性： 稳定
    :param arr: List[int]
    :return: arr
    """
    num_buckets = len(arr)
    buckets = [list() for _ in range(num_buckets)]
    for value in arr:
        index = value * num_buckets // (max(arr) + 1)
        buckets[index].append(value)

    result_arr = []
    for i in range(num_buckets):
        result_arr.extend(next_sort(buckets[i]))
    return result_arr


def next_sort(arr):     # use insertion_sort
    for i in range(1, len(arr)):
        e = arr[i]
        index = i
        while index >= 1 and arr[index-1] > e:
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = e
    return arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(bucket_sort(test_arr))
