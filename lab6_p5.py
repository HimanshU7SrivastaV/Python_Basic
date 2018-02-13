print "enter the value in list : "
i=0
b=[]
while i<10:
    a=input()
    b=b+[a,]
    i=i+1
min=b[0]
max=b[0]
j=0
while j<10:
    if b[j]>max:
        max=b[j]
    if b[j]<min:
        min=b[j]
    j=j+1
print "max of list is : ",max;
print "min of list is : ",min;
