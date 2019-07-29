def commonChars(A):
    """
    问题描述：给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符
    （包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，
    则需要在最终答案中包含该字符 3 次。
    你可以按任意顺序返回答案。
    解决思路：两两单词比较，得出最小公共集
    :param A:
    :return:
    """
    check = list(A[0])
    for word in A:
        new_check = []
        for c in word:
            if c in check:
                new_check.append(c)
                check.remove(c)
        check = new_check
    return check


if __name__ == "__main__":
    test_arr = ["cool","lock","cook"]
    print(commonChars(test_arr))
