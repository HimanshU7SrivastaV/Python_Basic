class employee:
    def __init__(self,a,b):
        self.name=a
        self.empcode=b
    def display(self):
        print 'your name is ',self.name
        print ' your employee code is : %s'%self.empcode
