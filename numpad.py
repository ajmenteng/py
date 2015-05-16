def conversion(a,t):
    l=len(t)
    key=t[0]
    temp=key
    word=''
    for i in range(1,l):
        if(key==t[i]):
            temp += t[i]
        else:
            if(key=='9'): m=4
            else: m=3
            idx = len(temp)%m
            if(idx==0):idx=m
            word += a[key][idx-1]
            key = t[i]
            temp = key
            
    if(key=='9'): m=4
    else: m=3
    idx = len(temp)%m
    if(idx==0):idx=m
    word += a[key][idx-1]
    
    return word

arr={'2':['A','B','C'],
    '3':['D','E','F'],
    '4':['H','I','J'],
    '5':['K','L','M'],
    '6':['N','O','P'],
    '7':['Q','R','S'],
    '8':['T','U','V'],
    '9':['W','X','Y','Z'],
    '#':' '}
    
t="222#3#99999#229"
print(conversion(arr,t))