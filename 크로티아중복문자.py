arr = input()
c = 0
check = 0
for i in range(int(len(arr))):
    if(i==int(len(arr))-1):
        if(check==0):
            c=c+1
            break;
    if(check >= 1):
        check =check-1
        pass
    else:
        if(arr[i]+arr[i+1] == 'c='):
            check=1
        elif(arr[i]+arr[i+1] == 'c-'):
            check=1
        elif(arr[i]+arr[i+1] == 'd-'):
            check=1
        elif(arr[i]+arr[i+1] == 'lj'):
            check=1
        elif(arr[i]+arr[i+1] == 'nj'):
            check=1
        elif(arr[i]+arr[i+1] == 's='):
            check=1
        elif(arr[i]+arr[i+1] == 'z='):
            check=1
        elif(i+2<int(len(arr))):
            if(arr[i]+arr[i+1]+arr[i+2] == 'dz='):
                check=2
        c=c+1
print(c)