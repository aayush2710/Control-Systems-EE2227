A = input().split()
A = [int(k) for k in A]
n = len(A) + 1

import numpy as np
RouthTable = [[],[]]
RouthTable[0] = A[0::2]
RouthTable[1] = A[1::2]
i=1
if len(RouthTable[0]) > len(RouthTable[1]):
  RouthTable[1].append(0)
while True:
  i+=1
  #RouthTable.append([])
  temp = []
  for j in range(1,len(RouthTable[i-2])):

      if(len(RouthTable[i-1]) < j+1):
          break
      if(RouthTable[i-1][0]==0):
          break
      k = -(RouthTable[i-2][0]*RouthTable[i-1][j] - RouthTable[i-2][j]*RouthTable[i-1][0])/RouthTable[i-1][0]
      temp.append(k)
  temp+=[0]*(len(RouthTable[i-2]) - len(temp))    
  RouthTable.append(temp)
  if i==len(A)-1:
      break
count = 0
sign = RouthTable[0][0]/abs(RouthTable[0][0])
for i in range(1,len(RouthTable)):

  if(RouthTable[i][0]/abs(RouthTable[i][0]))!=sign:
      count+=1
      sign = RouthTable[i][0]/abs(RouthTable[i][0])
print(RouthTable)
print("No of Poles in right half = " , count)
if(count > 0):
    print("Unstable")
else:
    print("Stable")