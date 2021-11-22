def bi_search(start, end):
    global res
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in range(1, n + 1):
            temp += min(n, mid // i)
            # mid // i 를 하는 이유?
            # 해당행에서 mid보다 작은 수를 구하는 방법은
            # mid / i 를 하면 해당 행에서 mid보다 작은 수의 개수를 찾을 수 있음
            # 하지만 3*3에서 행에 최대 개수는 3인데
            # 6/1 을 할 경우에는 6개가 나와서
            # mid / i 의 값이n의 값보다 커질경우
            # 최대개수인 n을 삽입하는것임
        if temp >= m:
            # mid보다 작은수의 개수가 m이랑 같거나 크면
            # 더 작아져야하기 때문에 end값을 낮춰줌
            res = mid
            end = mid - 1
        else:
            start = mid + 1


n = int(input())
m = int(input())
arr = []
res = 0
bi_search(1, m)
print(res)
