def degpow(n,p)
s=0
ch=str(n)
for i in range (len(ch))
   s+=int(ch[i])**p
   p+=1
k=s/n
if type(k)==int
   return k
else 
   return -1

   
