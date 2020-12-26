
ch=input()
s=""
j=0
for i in range (len(ch)):
    if ch[i]=='A':
        s[j]=ch[i]
        j+=1
    elif ch[i]=='Z':
        for k in range (25):
            s[j]=' '
            j+=1
        s[j]=ch[i]
        j+=1
    else :
        s[j]=' '
        s[j+1]=ch[i]
        j+=2
print(s)     
