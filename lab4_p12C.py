print "now we r gonna print a new design : "
n=6
for i in range (6):
    for j in range(6):
        if j<(n-(i+1)):
            print " ",
        else:
            print "*",
    print ""
    j=j-1
