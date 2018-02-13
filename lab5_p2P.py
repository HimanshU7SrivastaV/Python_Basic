def prime(n):
    c=0
    i=1
    for i in range(n):
        if n%i==0 :
            c=c+1
    return (c)
        
n=input('enter the number : ')
x=prime(n)
if x==1 :
    print "number is prime "
else :
    print "number is not prime "
