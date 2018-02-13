def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)

print "enter the value to find factorial :"
n=input()
x=facto(n)
print "factorial of that number is :",x;
