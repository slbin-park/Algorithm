number = int(input())
count =0 
if(number<100):
    print(number)
elif(number>100 and 110>number):
    print(99)
else:
    for i in range(111,number+1):
        b = i//100 #100의 자리
        c = i%100//10 #10의 자리
        d = i%10 #1의자리
        if((b-c) == (c-d)):
            count=count+1
        elif((c-b) == (d-c)):
            count= count+1
    print(99+count)

