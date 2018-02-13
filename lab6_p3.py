print "enter the value in tuple : "
i=0
b=[]
while i<10:
    a=input()
    b=b+[a,]
    i=i+1
(b[0],b[9])=(b[9],b[0])
while i<=10:
    print b
    i=i+1

    
