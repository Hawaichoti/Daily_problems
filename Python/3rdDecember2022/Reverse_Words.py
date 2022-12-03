def reverse(a): #Reverse is a function to reverse the words of a given string
    b=a.split()
    c = ""
    for i in reversed(b):
        c = c+" "+i 
    return c
    

S1 = input("Enter a string")#taking a string as input


print(reverse(S1))
