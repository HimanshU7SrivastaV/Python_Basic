class age:
    def __init__(self,a,b):
        self.year=a
        self.month=b
    def find_age(self):
        self.yr=2016-self.year
        if(self.month<12):
            self.mn=(self.month%11)
        else:
            self.yr=self.yr-1
            self.mn=11
        print 'you are %s year and'%self.yr,
        print '%s months old'%self.mn
        
        
