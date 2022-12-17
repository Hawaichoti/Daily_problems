import math
def mean(a,n):
  sum = 1
  for j in range(n):
    sum = sum * a[j]
  mean = math.pow(sum,(1/n))
  return mean
  

s = int(input("Enter a number"))
print("Enter numbers in list")
a=[]
for i in range(s):
  a.append(int(input("")))

m = mean(a,s)
print(m,"is mean")


