def allCellsDistOrder(R, C, r0, c0):
    """
    问题描述： 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
    另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，
    其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
    解决思路： 按照曼哈顿距离进行排序即可
    :param R:
    :param C:
    :param r0:
    :param c0:
    :return:
    """
    def distance(cell):
        i, j = cell
        return abs(i - r0) + abs(j - c0)

    cells = [(i, j) for i in range(R) for j in range(C)]
    return sorted(cells, key=distance)


if __name__ == "__main__":
    print(allCellsDistOrder(R=3, C=3, r0=1, c0=1))
