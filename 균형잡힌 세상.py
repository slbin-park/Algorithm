from collections import deque
while(True):
    texto = True
    text = input()
    textc=deque() # 덱 생성
    if(text=='.'):
        break;
    for i in range(int(len(text))):
        if(text[i] == '[' or text[i] == '('):
            textc.append(text[i])
        elif(text[i] == ']'):
            if(len(textc)==0):
                texto=False
                break;
            elif('[' == textc.pop()):
                continue;
            else:
                texto=False
                break;
        elif(text[i] == ')'):
            if(len(textc)==0):
                texto=False
                break;
            elif('(' ==textc.pop()):
                continue;
            else:
                texto=False
                break;
    if(len(textc)!=0):
        texto=False;
    if(texto):
        print('yes')
    else:
        print('no')



# dq=deque() # 덱 생성
# dq.append() # 덱의 가장 오른쪽에 원소 삽입
# dq.popleft() # 가장 왼쪽 원소 반환
# dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입
# dp.pop() # 가장 오른쪽 원소 반환
# dp.clear() # 모든 원소 제거
# dp.copy() # 덱 복사
# dp.count(x) #x와 같은 원소의 개수를 계산