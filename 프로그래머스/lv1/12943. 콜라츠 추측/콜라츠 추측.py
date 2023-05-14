def solution(num):
    answer = -1
    n = 500
    while n:
        if num==1:
            break
        n-=1;
        if num%2==0:
            num = num//2
        else:
            num = num*3+1
    return 500-n if n!=0 else -1