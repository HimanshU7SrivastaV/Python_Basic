class distance:
    def __init__(self,a,b):
        self.ft=a
        self.inch=b
    def add(self):
        self.inch=self.ft*0.083+self.inch
        print 'total distance in inches is  : %s'%self.inch
    def display(self):
        print 'total distance in feet is : %s'%self.ft
        print 'total distance in inches is : %s'%self.inch
