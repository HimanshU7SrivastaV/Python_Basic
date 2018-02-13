def prime(a,b):
    c=0
    i=a
    if a<b:
        for i in range(b):
            if a%i==0:
                c=c+1
        if c==1:
            print a
        a=a+1
a=input('enter the number : ')
b=input('enter the second number greater than 1st  : ')
prime(a,b)
