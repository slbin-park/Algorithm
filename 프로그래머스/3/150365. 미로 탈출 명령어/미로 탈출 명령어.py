import sys

sys.setrecursionlimit(10**5)

dirs = [["d", 1, 0], ["l", 0, -1], ["r", 0, 1], ["u", -1, 0]]


def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k:
        return "impossible"
    if dist % 2 is not k % 2:
        return "impossible"

    def dfs(cy, cx, path, cnt):
        if cnt == k:
            if cy == r and cx == c:
                return path
        else:
            for prc in dirs:
                ny = cy + prc[1]
                nx = cx + prc[2]
                if 1 <= ny <= n and 1 <= nx <= m:
                    dist = abs(ny - r) + abs(nx - c)
                    if dist > k - (cnt + 1):
                        continue
                    rtn = dfs(ny, nx, path + prc[0], cnt + 1)
                    if rtn is not None:
                        return rtn

    answer = dfs(x, y, "", 0)
    if answer is None:
        return "impossible"
    return answer