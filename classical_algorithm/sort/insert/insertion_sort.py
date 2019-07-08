def insertion_sort(arr):
    """

    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(1, n):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = cursor
    return arr
