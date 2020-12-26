def degpow(n,p) :
ch=str(n)
s=0
for i in range (len(ch))
   s+=int(ch[i])**p
   p+=1
k=s/n
if type(k)==int
   return k
else 
   return -1
while True
  n=int(input("donner un entier positive "))
  if n>0
    return n
while True
  p=int(input("donner un entier positive "))
  if p>0
    return p
k=degpow(n,p)
print (k)
