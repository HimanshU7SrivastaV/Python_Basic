def compound_intrest(p,r,t):
    return(p*((1+r/100)**t))


print "enter the value of p ,r , t:"
p=input()
r=input()
t=input()
ci=compound_intrest(p,r,t)
print "compound intrest is :",ci;
