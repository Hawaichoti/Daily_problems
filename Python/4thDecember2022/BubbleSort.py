def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if(j+1<len(a)):
                if(a[j]>a[j+1]):
                    b = a[j]
                    a[j] = a[j+1] 
                    a[j+1] = b
        #print(a)
    return a
                
n = int(input("Enter the length of an array"))
print("Enter the elements of an array")
arr=[]
for i in range(n):
    arr.append(int(input()))
print(bubble(arr))
