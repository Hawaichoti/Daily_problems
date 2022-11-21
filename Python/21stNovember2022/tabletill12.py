#Program that prints a multiplication table for numbers up to 12.
for i in range(1,13):#this loop is providing the number whose table is getting printed
    for j in range(1,11):#this loop is providing the number from 1 to 10
        print(str(i)+" * "+str(j)+" = "+str(i*j))#printing the table
    print("\n")
