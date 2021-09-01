A,B,V = map(int,input().split())
count =1;
while 1 :
    if(A*count -B*(count-1)>=V):
        break;
    count=count+1
print(count)