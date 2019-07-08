s = int(inpuut())
k=1
for j in range(len(s)-1):
  b=s[j]+s[j+1]
  p=int(b)
  if p<=26 and s[j]!="0":
    k+=1
if k==3:
  print(k)
else:
  print(k+(k-1)//2)

               
