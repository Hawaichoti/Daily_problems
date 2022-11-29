N = int(input("Enter the number whose factorial has to be calculated"))# Taking input from user
if((N>=1)and(N<=10)):
    for i in range(1,N+1):
        prod = prod * i
print(prod)  
