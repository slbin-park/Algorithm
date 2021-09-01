from collections import deque
a,b = map(int,input().split())
arr = deque() 
for i in range(int(a)):
    arr.append(i+1)
print('<',end='')
for i in range(int(a)):
    for j in range(int(b-1)):
        arr.append(arr.popleft())
    if(len(arr)==1):
        print(arr.popleft(),end='')
        break;
    print(arr.popleft(),end=', ')
print('>',end='')

# print('<',end='')
# for i in range(int(len(arr2))):
#     print(arr2[i],end=',')
# print('>')

# dq=deque() # 덱 생성
# dq.append() # 덱의 가장 오른쪽에 원소 삽입
# dq.popleft() # 가장 왼쪽 원소 반환
# dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입
# dp.pop() # 가장 오른쪽 원소 반환
# dp.clear() # 모든 원소 제거
# dp.copy() # 덱 복사
# dp.count(x) #x와 같은 원소의 개수를 계산