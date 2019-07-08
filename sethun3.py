s = int(input())
n = list(map(int,input().split()))
temp=[]
for i in range(s):
  if n[i] == i:
    temp.append(n[i])
if len(temp) == 0:
  print(-1)
else:
  for i in sorted(temp):
    print(i,end=' ')
