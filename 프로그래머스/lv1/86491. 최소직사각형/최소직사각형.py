def solution(sizes):
    answer = 0
    w = []
    h = []
    for a,b in sizes:
        if a>=b:
            w.append(a)
            h.append(b)
        else:
            w.append(b)
            h.append(a)
        
        
    return max(w)*max(h)