def radix_sort(arr):
    """
    算法思想： 按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。
    时间复杂度： O(n*k),k是常数
    空间复杂度： O(n+k)
    稳定性： 稳定
    :param arr: List[int]
    :return: arr
    """
    placement = 1
    max_number = max(arr)

    while placement < max_number:
        buckets = [list() for _ in range(10)]
        for num in arr:
            digit_number = num // placement % 10
            buckets[digit_number].append(num)

        index = 0
        for bucket in buckets:
            for num in bucket:
                arr[index] = num
                index += 1

        placement *= 10

    return arr


if __name__ == "__main__":
    test_arr = [8, 5, 10, 12, 7, 6, 15, 9, 11, 3]
    print(radix_sort(test_arr))

