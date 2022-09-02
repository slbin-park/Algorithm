n = int(input())
a0 =[1,0,1]
a1 =[0,1,1]

def fib(n):
    if(len(a0) <= n):
        for i in range(len(a0),n+1):
            a0.append(a0[i-1]+a0[i-2])
            a1.append(a1[i-1]+a1[i-2])
    print(a0[n],a1[n])
    

for _ in range(n):# 1부터 5까지
    a= int(input())
    fib(a)