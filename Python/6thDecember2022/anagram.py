def anagram(a,b):
    if(len(a)==len(b)):
        sorted(a)
        sorted(b)
        if(sorted(a)==sorted(b)):
            return 0
        else:
            return 1

st1 = input("Enter a string")
st2 = input("Enter another string")
c = anagram(st1,st2)
if(c==0):
    print(st1+" and "+st2+" are anagram")
else:
    print(st1+" and "+st2+" are not anagram")
