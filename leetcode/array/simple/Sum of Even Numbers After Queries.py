def sumEvenAfterQueries(A, queries):
    """
    问题描述：给出一个整数数组 A 和一个查询数组 queries。
    对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，
    我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中偶数值的和。
    （此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）
    返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。
    解决思路：先算出初始偶数之和，接着遍历查询数组，保留相加之前的prev，若prev为偶数则减去，
    所相加之后的value为偶数，则加上
    :param A:List[int]
    :param queries:List[List[int]]
    :return:List[int]
    """
    res = []
    total = sum(v for v in A if v % 2 == 0)
    for v, i in queries:
        prev = A[i]
        A[i] += v
        if prev % 2 == 0:
            total -= prev
        if A[i] % 2 == 0:
            total += A[i]
        res.append(total)
    return res


if __name__ == "__main__":
    test_arr = [1,2,3,4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumEvenAfterQueries(test_arr, queries))
