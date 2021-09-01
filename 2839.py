m = int(input())
a = m%10
b = int(m/5)
if(a==1):
    print(b+1)
elif(a==2):
    print(b+2)
elif(a==3):
    print(b+1)
elif(a==4):
    if(m<10):
        print(-1) 
    else:
        print(b+2)
elif(a==6):
    print(b+1)
elif(a==7):
    if(m<10):
        print(-1)
    else:
        print(b+2)
elif(a==8):
        print(b+1)
elif(a==9):
        print(b+2)
else:
    print(b)



# 1은 -1 +2 
# 2는 +3
# 3은 +1 
# 4는 -1 + 3 
# 5그대로
# 6은 -1 +2 
# 7은 -5 +9 
# 8은 -3 +6 
# 9는 -1 +3