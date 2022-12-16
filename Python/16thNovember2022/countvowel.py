s = input("Enter a string")
c=0
for i in s:
  if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
    c=c+1
print("There are",c,"vowels present in",s)
