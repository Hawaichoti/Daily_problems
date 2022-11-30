def blackjack(a,b):
  
  if(a+b>21):
    return 0
  else:
    return a+b  

a = int(input("Enter a number between 1 to 13"))
b = int(input("Enter a number between 1 to 13"))
sum = blackjack(a,b)
print(sum)
