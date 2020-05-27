n=int(input('enter the num'))
for i in range (n):
    l=[]
    s=list(input().split())
    l.append(sorted(s[0]))
    l.append(sorted(s[1]))
    if(l[0]==l[1]):
        print('yes')
    else:
        print('no')
    
