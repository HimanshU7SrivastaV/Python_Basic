def convert_temp(f):
    return (f-32)*5.0/9.0

print "enter the temp into fornh :"
f=input()
x=convert_temp(f)
print "temp in celc is :",x;
