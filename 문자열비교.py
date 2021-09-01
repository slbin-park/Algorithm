while True:
    text = str(input())
    check = False
    if(text==str(0)):
        break;
    elif(len(text)==1):
        check= True;
    elif(len(text)%2 == 0):
        for i in range(int(len(text)/2)):
            if(text[i]==text[int(len(text))-1-i]):
                if(i==int(len(text)/2)-1):
                    check = True;
                continue;
            else:
                break;
    else :
        for i in range(int(len(text)/2)):
            if(text[i]==text[int(len(text))-1-i]):
                if(i==int(len(text)/2)-1):
                    check = True;
                continue;
            else:
                break;
    if(check):
        print('yes')
    else :
        print('no')            
