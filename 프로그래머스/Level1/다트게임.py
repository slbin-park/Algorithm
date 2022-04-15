def solution(dartResult):
    answer = 0
    i = 0
    dp = [0 for i in range(3)]
    dp_n = 0
    while i < len(dartResult):
        cur = 0
        cur_n = int(dartResult[i])
        if dartResult[i].isdigit():
            if dartResult[i + 1].isdigit():
                cur_n = int(dartResult[i] + dartResult[i + 1])
                i += 1
            if dartResult[i + 1] == 'S':
                cur = cur_n
            elif dartResult[i + 1] == 'D':
                cur = cur_n**2
            else:
                cur = cur_n**3
        if i + 2 < len(dartResult):
            if dartResult[i + 2] == '#':
                cur = cur * (-1)
                i += 3
            elif dartResult[i + 2] == '*':
                if dp_n > 0:
                    dp[dp_n - 1] = dp[dp_n - 1] * 2
                cur = cur * 2
                i += 3
            else:
                i += 2
        else:
            i += 2
        dp[dp_n] = cur
        dp_n += 1
    return sum(dp)