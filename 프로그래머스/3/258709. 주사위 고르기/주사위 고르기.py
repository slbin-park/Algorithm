from itertools import combinations
from itertools import product
import bisect

def solution(dice):
    answer = []
    arr = []
    dic = {}
    win = 0

    def sum_selected_dices(dice, dices_idx):
        """
        dice: 주사위 전체 (2차원 리스트)
        dices_idx: 선택할 주사위 인덱스 배열 (예: [1,3])
        return: 선택한 주사위들로 만들 수 있는 모든 합 (중복 포함)
        """
        selected = [dice[i] for i in dices_idx]   # 해당 주사위만 추출
        cases = product(*selected)                # 모든 경우의 수
        sums = [sum(case) for case in cases]      # 합 구하기
        return sums

    

    def split_combinations(dice):
        n = len(dice)
        assert n % 2 == 0, "dice 개수는 짝수여야 합니다."
        half = n // 2
        result = []

        # 0번 인덱스를 A그룹에 고정 → 나머지에서 half-1개만 고르면 됨
        for comb in combinations(range(1, n), half - 1):
            groupA = [0, *comb]
            groupB = [i for i in range(n) if i not in groupA]
            result.append([groupA, groupB])

        return result
    
    def compare_counts_fast(arr1, arr2):
        arr2_sorted = sorted(arr2)
        result = []
        for val in arr1:
            left = bisect.bisect_left(arr2_sorted, val)   # val보다 작은 개수
            right = bisect.bisect_right(arr2_sorted, val) # val 이하 개수
            smaller = left
            equal = right - left
            bigger = len(arr2_sorted) - right
            result.append([smaller, equal, bigger])
        return result

        
    pairs = split_combinations(dice)
    # print(pairs)
    for pair in pairs:
        # print(pair)
        arr1 = sum_selected_dices(dice,pair[0])
        arr2 = sum_selected_dices(dice,pair[1])
        result = compare_counts_fast(arr1,arr2)
        curwin = 0
        curdraw = 0
        curlose = 0
        for a in result:
            curwin += a[0]
            curdraw += a[1]
            curlose += a[2]
        if win < curwin:
            win = curwin
            answer = pair[0]
        if win < curlose:
            win = curlose
            answer = pair[1]
        
        # print(win,draw,lose)
        
        # print(result)
    realAnswer = []
    for i in range(len(answer)):
        realAnswer.append(answer[i]+1)
    return realAnswer