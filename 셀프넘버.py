n = int(input())
count = n
for i in range(0,n):
    a = input() 
    for j in range(0,int(len(a))-1):
        if a[j]==a[j+1]:
            pass
        elif a[j] in a[j+1:]:
            print('a = ',a[j+1:]) #j부터 뒤에까지의 배열을 반환함
            count-=1
            break
print(count)

