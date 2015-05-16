a=[8,2,4,9,3,8]
for j in range(1,len(a)):
    i=j-1
    while (a[i+1]<a[i]) and i>=0:
        temp=a[i+1]
        a[i+1]=a[i]
        a[i]=temp
        i-=1
print(a)