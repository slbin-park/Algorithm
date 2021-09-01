n = int(input())
b = float

for i in range(n):
    b=0
    count =0
    li = list(map(float,  input().split()))
    for a in range(1,len(li)):
        b+=li[a]
    for i in range(1,len(li)):
        if li[i] > b/li[0] :
            count=count+1
    print("{:.3f}%".format(round(count/li[0]*100,3)))