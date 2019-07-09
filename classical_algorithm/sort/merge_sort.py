def merge_sort(arr):
    """
    算法思想： 归并排序是利用归并的思想实现的排序方法，该算法采用经典的分治策略（分治法将问题分
    成一些小的问题然后递归求解，而治的阶段则将分的阶段得到的各答案"修补"在一起，即分而治之)。
    时间复杂度： O(nlogn)
    空间复杂度： O(n)
    稳定性： 稳定
    :param arr: List[int]
    :return: arr
    """
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def merge(left, right, temp_arr):
    """
    将两个有序序列合并， 时间复杂度为O(n)
    :param left:
    :param right:
    :param temp_arr:
    :return:
    """
    left_pos, right_pos = 0, 0

    while left_pos < len(left) and right_pos < len(right):
        if left[left_pos] <= right[right_pos]:
            temp_arr[left_pos + right_pos] = left[left_pos]
            left_pos += 1
        else:
            temp_arr[left_pos + right_pos] = right[right_pos]
            right_pos += 1

    for left_pos in range(left_pos, len(left)):
        temp_arr[left_pos + right_pos] = left[left_pos]

    for right_pos in range(right_pos, len(right)):
        temp_arr[left_pos + right_pos] = right[right_pos]

    return temp_arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(merge_sort(test_arr))
