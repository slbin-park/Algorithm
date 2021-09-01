
while True:
    li = list(map(int,input().split()))
    li.sort()
    a= li[0]
    b= li[1]
    c= li[2]
    if(a==0 and b==0 and c==0):
        break;
    elif(a==0 or b==0 or c==0):
        print('wrong')
    elif((a*a)+(b*b)==(c*c)):
        print('right')
    else:
        print('wrong')