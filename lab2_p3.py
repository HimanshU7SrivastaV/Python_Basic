print"enter the rate , principle value and time"
p=input()
r=input()
t=input()
ci=p*((1+r/100)**t)
si=(p*r*t)/100
print"simple intrest is :",si;
print"compound intrest is :",ci;
