print "we gonna maintain the bamk account : "
a=input('enter the balance in current account : ')
b=input('enter the balance in savings account : ')
print "1) withdrawl "
print "2) deposit "
x=input('enter ur choice what do you want :')
if x==1:
    print "1) current account "
    print "2) savings account "
    print "enter your choice to withdrawl money : "
    ch=input()
    m=input('enter the money : ')
    if ch==1 :
        if (a-m)>10000 :
            print " your transection is successful "
            c=a-m
            print "your new account balance is : "
            print c
        else :
            print "SORRY !!! minimum account bal is 10000 "
            print "your transection is unsuccessful ..."
    if ch==2 :
        if (b-m)>1000 :
            print " your transection is successful "
            c1=b-m
            print "your new account balance is : "
            print c1
        else :
             print "SORRY !!! minimum account bal is 1000 "
             print "your transection is unsuccessful ..."
    else :
        print "please enter the valid key ...... "
if x==2:
    print "1) current account "
    print "2) savings account "
    print "enter your choice to deposite your money : "
    ch=input()
    mn=input('enter the money :')
    if ch==1:
        a=a+mn
        print "you are successfully deposited your money ..."
        print "now your current balance is : ",
        print a
    if ch==2:
        b=b+mn
        print "you are successfully deposited your money ..."
        print "now your savings balance is : ",
        print b
    else:
        print "please enter the valid choice ......"
else:
    print "SORRY !!!! please enter the valid choice ......."
