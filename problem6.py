while True :
  n=int (input("donner un entier"))
  if (n>=0)and (n<10000) :
    break 
if n!=0:
 for i in range (n):
    ch+='('
 for i in range (n):
    ch+=')'
else :
    ch='.'
print (ch)    
    
