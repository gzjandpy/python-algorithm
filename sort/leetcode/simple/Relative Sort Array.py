def relativeSortArray(arr1, arr2):
    """
    问题描述：给你两个数组，arr1 和 arr2，arr2 中的元素各不相同,arr2 中的每个元素都出现在 arr1 中
    对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
    未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
    解决方法：利用sorted函数的关键字key制造一个函数
    :param arr1:
    :param arr2:
    :return:
    """
    def compare(number):
        if number in arr2:
            return arr2.index(number)
        else:
            return len(arr2) + number

    return sorted(arr1, key=compare)
    """
    利用空间换时间：
        A = [i for i in arr1 if i in arr2]
        B = [i for i in arr1 if i not in arr2]
        
        def compare(number):
            return arr2.index(number)
        
        A.sort(key=compare)
        B.sort()
        return A+B
    """


if __name__ == "__main__":
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(relativeSortArray(arr1, arr2))
