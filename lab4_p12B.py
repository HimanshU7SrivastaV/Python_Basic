print "now we are printing a design :"
for i in range(21):
    if i%5==0:
        for j in range(21):
            if j%5==0 :
                print "+",
            else:
                print "-",
        print ''
    else :
        
        if i%5!=0 :
            for j in range(21):
                if j%5==0 :
                    print '|',
                else:
                    print ' ',
            print ''
